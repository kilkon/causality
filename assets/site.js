(function () {
  var body = document.body;
  var toggle = document.querySelector("[data-nav-toggle]");
  var editorConfig = window.__BOOK_EDITOR__ || null;
  var root = document.querySelector("[data-editor-root]");
  var currentLink = document.querySelector(".sidebar-link[aria-current='page']");
  var openSourceButtons = document.querySelectorAll("[data-open-source]");
  var openPathButtons = document.querySelectorAll("[data-open-path]");
  var feedbackForms = document.querySelectorAll("[data-feedback-form]");
  var protocol = window.location.protocol;
  var canUseApi = protocol === "http:" || protocol === "https:";
  var editorHeaders = {
    "X-Book-Editor": "1"
  };

  if (toggle) {
    toggle.addEventListener("click", function () {
      body.classList.toggle("nav-open");
    });
  }

  if (currentLink) {
    window.requestAnimationFrame(function () {
      currentLink.scrollIntoView({ block: "center", inline: "nearest" });
    });
  }

  function setStatus(message, kind) {
    var status = document.querySelector("[data-editor-status]");
    if (!status) return;
    status.textContent = message;
    status.dataset.kind = kind || "neutral";
  }

  async function openTarget(payload, statusTarget) {
    if (!canUseApi) {
      if (statusTarget) {
        statusTarget.textContent = "localhost 서버에서만 파일 열기가 동작합니다.";
      }
      return;
    }

    try {
      var response = await fetch("/__api/open", {
        method: "POST",
        headers: Object.assign({ "Content-Type": "application/json" }, editorHeaders),
        body: JSON.stringify(payload)
      });
      var result = await response.json();
      if (!response.ok || !result.ok) {
        throw new Error(result.error || "open_failed");
      }
      if (statusTarget) {
        statusTarget.textContent = "로컬 편집기로 파일을 열었습니다.";
      }
      setStatus("로컬 편집기로 파일을 열었습니다.", "success");
    } catch (error) {
      if (statusTarget) {
        statusTarget.textContent = "파일을 열지 못했습니다.";
      }
      setStatus("파일을 열지 못했습니다.", "error");
    }
  }

  openSourceButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var slug = button.getAttribute("data-open-source");
      openTarget(
        { slug: slug },
        document.querySelector("[data-open-source-status=\"" + slug + "\"]")
      );
    });
  });

  openPathButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var path = button.getAttribute("data-open-path");
      openTarget(
        { path: path },
        document.querySelector("[data-open-path-status=\"" + path + "\"]")
      );
    });
  });

  function buildFeedbackMailto(form) {
    var email = form.getAttribute("data-feedback-email") || "";
    var subject = form.getAttribute("data-feedback-subject") || "의견";
    var page = form.getAttribute("data-feedback-page") || "";
    var slug = form.getAttribute("data-feedback-slug") || "";
    var nickname = (form.querySelector("[name='nickname']") || {}).value || "";
    var replyEmail = (form.querySelector("[name='reply_email']") || {}).value || "";
    var scope = (form.querySelector("[name='scope']") || {}).value || "";
    var message = (form.querySelector("[name='message']") || {}).value || "";

    var bodyLines = [
      "책/절: " + page,
      "파일: " + slug + ".html",
      "의견 범위: " + scope,
      "이름 또는 별명: " + (nickname.trim() || "익명"),
      "답장 이메일: " + (replyEmail.trim() || "미기재"),
      "",
      "[의견]",
      message.trim()
    ];

    return "mailto:" + encodeURIComponent(email) +
      "?subject=" + encodeURIComponent(subject) +
      "&body=" + encodeURIComponent(bodyLines.join("\n"));
  }

  feedbackForms.forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var messageField = form.querySelector("[name='message']");
      if (!messageField || !messageField.value.trim()) {
        if (messageField) {
          messageField.focus();
        }
        return;
      }
      window.location.href = buildFeedbackMailto(form);
    });
  });

  if (!root || !editorConfig) {
    return;
  }

  var openButton = document.querySelector("[data-editor-open]");
  var closeButton = document.querySelector("[data-editor-close]");
  var loadButton = document.querySelector("[data-editor-load]");
  var saveButton = document.querySelector("[data-editor-save]");
  var textarea = document.querySelector("[data-editor-textarea]");
  var hint = document.querySelector("[data-editor-hint]");

  function getEditorLoadUrl() {
    if (editorConfig.path) {
      return "/__api/file?path=" + encodeURIComponent(editorConfig.path);
    }
    return "/__api/chapter?slug=" + encodeURIComponent(editorConfig.slug);
  }

  function getEditorSaveUrl() {
    return editorConfig.path ? "/__api/file" : "/__api/chapter";
  }

  function getEditorSavePayload() {
    if (editorConfig.path) {
      return {
        path: editorConfig.path,
        content: textarea.value
      };
    }
    return {
      slug: editorConfig.slug,
      content: textarea.value
    };
  }

  function getOpenStatusTarget() {
    if (editorConfig.path) {
      return document.querySelector("[data-open-path-status=\"" + editorConfig.path + "\"]");
    }
    return document.querySelector("[data-open-source-status=\"" + editorConfig.slug + "\"]");
  }

  function openPanel() {
    root.hidden = false;
    body.classList.add("editor-open");
  }

  function closePanel() {
    root.hidden = true;
    body.classList.remove("editor-open");
  }

  async function loadMarkdown() {
    if (!canUseApi) {
      setStatus("편집 기능은 localhost 서버에서만 동작합니다.", "warn");
      return;
    }

    setStatus("원고를 불러오는 중입니다...", "neutral");
    try {
      var response = await fetch(getEditorLoadUrl(), {
        headers: editorHeaders
      });
      if (!response.ok) {
        throw new Error("load_failed");
      }
      var payload = await response.json();
      textarea.value = payload.content || "";
      setStatus("원고를 불러왔습니다.", "success");
    } catch (error) {
      setStatus("원고를 불러오지 못했습니다.", "error");
    }
  }

  async function saveMarkdown() {
    if (!canUseApi) {
      setStatus("편집 기능은 localhost 서버에서만 동작합니다.", "warn");
      return;
    }

    setStatus("저장하고 다시 빌드하는 중입니다...", "neutral");
    saveButton.disabled = true;
    try {
      var response = await fetch(getEditorSaveUrl(), {
        method: "POST",
        headers: Object.assign({ "Content-Type": "application/json" }, editorHeaders),
        body: JSON.stringify(getEditorSavePayload())
      });
      var payload = await response.json();
      if (!response.ok || !payload.ok) {
        throw new Error(payload.error || "save_failed");
      }
      setStatus("저장되었습니다. 페이지를 새로고침하면 최신 빌드가 보입니다.", "success");
      var openStatus = getOpenStatusTarget();
      if (openStatus) {
        openStatus.textContent = "저장되었습니다.";
      }
    } catch (error) {
      setStatus("저장에 실패했습니다.", "error");
    } finally {
      saveButton.disabled = false;
    }
  }

  if (!canUseApi && hint) {
    hint.textContent =
      "이 페이지를 file://로 열면 편집 기능이 동작하지 않습니다. `python scripts\\serve.py`로 실행한 localhost 페이지에서 사용해 주세요.";
  }

  if (openButton) {
    openButton.addEventListener("click", function () {
      openPanel();
      if (!textarea.value) {
        loadMarkdown();
      }
    });
  }

  if (closeButton) {
    closeButton.addEventListener("click", closePanel);
  }

  if (loadButton) {
    loadButton.addEventListener("click", loadMarkdown);
  }

  if (saveButton) {
    saveButton.addEventListener("click", saveMarkdown);
  }

  document.addEventListener("keydown", function (event) {
    var isSave = (event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "s";
    if (!isSave) return;
    if (!body.classList.contains("editor-open")) return;
    event.preventDefault();
    saveMarkdown();
  });
})();
