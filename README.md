# causal inference2

기존 정적 HTML 전자책을 보존한 채, Markdown 원고 기반으로 다시 빌드하는 작업 폴더입니다.

## 구조

```text
causal inference2/
  assets/
    site.css
    site.js
  content/
    book.json
    chapters/
      *.md
  dist/
  scripts/
    build.py
    import_legacy.py
    serve.py
    watch.py
```

## 로컬 편집

일반 빌드:

```bash
python scripts/build.py
```

로컬 편집 서버:

```bash
python scripts/serve.py
```

브라우저에서 아래 주소를 엽니다.

```text
http://127.0.0.1:8000
```

이 로컬 서버에서만 `브라우저에서 편집`, `표지 메타 열기`, `Markdown 열기` 버튼이 보이고 동작합니다.

자동 재빌드:

```bash
python scripts/watch.py
```

## 공개 배포

공개 배포판은 읽기 전용으로 빌드합니다.

```bash
python scripts/build.py --public
```

이 모드에서는 다음이 적용됩니다.

- 편집 버튼이 HTML에 포함되지 않습니다.
- 브라우저 편집 패널이 생성되지 않습니다.
- GitHub Pages 배포용 `.nojekyll` 파일이 `dist/`에 함께 생성됩니다.

배포 대상은 `dist/` 폴더입니다.

## GitHub Pages

`.github/workflows/deploy-pages.yml`이 포함되어 있습니다. 이 워크플로는 다음을 수행합니다.

1. 저장소를 체크아웃합니다.
2. Python을 설정합니다.
3. `python scripts/build.py --public`으로 공개용 사이트를 빌드합니다.
4. `dist/`를 GitHub Pages로 배포합니다.

GitHub에서 한 번만 아래를 켜주면 됩니다.

1. 저장소 `Settings`
2. `Pages`
3. `Build and deployment`를 `GitHub Actions`로 설정

이후 `main` 브랜치에 푸시하면 자동 배포됩니다.
