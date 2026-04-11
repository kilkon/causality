---
title: 3.3 식별: 관측분포와 인과량의 연결
description: 식별은 가정이 맞다면 인과량을 관측 데이터만으로 표현할 수 있는지를 묻는 문제다. 이 절은 관측분포와 인과량을 잇는 식별의 핵심 직관을 정리한다.
---

# 3.3 식별: 관측분포와 인과량의 연결
3.2절에서 구조를 설정했다면 이제 핵심 질문은 이것이다. “그 구조와 가정 아래, 우리가 알고 싶은 인과량을 관측 데이터만으로 계산할 수 있는가?” 이 질문이 바로 식별(identification)의 문제다. 식별은 알고리즘보다 먼저 오는 논리 문제이며, 같은 데이터라도 어떤 질문과 어떤 가정을 택했는지에 따라 성립 여부가 달라진다.

## 3.3 식별: 관측분포와 인과량의 연결

      식별은 “가정이 맞다면 인과량을 데이터로 계산할 수 있는가”의 문제다. 식별이 성립하면
      \(\theta=g(P)\) 꼴이 존재하고, 그 다음에야 추정량 \(\hat\theta=g(\hat P_n)\)를 논의할 수 있다.

    \[
      \theta=\mathbb{E}[Y(1)-Y(0)],\quad
      \{Y(1),Y(0)\}\perp\!\!\!\perp D\mid X
      \Rightarrow
      \theta=\mathbb{E}\!\left[\mathbb{E}[Y\mid D=1,X]-\mathbb{E}[Y\mid D=0,X]\right].
    \]

:::

    ## 연구 사례: Oregon Health Insurance Experiment

      Oregon Medicaid lottery는 “복권 당첨(할당)”이라는 외생적 변동을 제공해 ITT를 강하게 식별한다.
      다만 실제 가입은 불완전해 LATE 해석으로 이동한다. 즉 같은 데이터에서도 질문을
      ATE로 둘지 LATE로 둘지에 따라 식별 표현이 달라진다.

<svg width="520" height="150" viewBox="0 0 520 150" xmlns="http://www.w3.org/2000/svg">
        <text x="260" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#1e4d6b">식별 트리</text>
        <rect x="25" y="40" width="150" height="42" rx="7" fill="#eef3f6" stroke="#1e4d6b"/>
        <text x="100" y="65" text-anchor="middle" font-size="11">질문: ATE?</text>
        <rect x="195" y="40" width="150" height="42" rx="7" fill="#edf7ef" stroke="#1d6b4a"/>
        <text x="270" y="65" text-anchor="middle" font-size="11">가정: 교환가능성</text>
        <rect x="365" y="40" width="130" height="42" rx="7" fill="#f6eef8" stroke="#6b4c9a"/>
        <text x="430" y="65" text-anchor="middle" font-size="11">식별: 표준화</text>
        <line x1="175" y1="61" x2="193" y2="61" stroke="#333" marker-end="url(#m33)"/>
        <line x1="345" y1="61" x2="363" y2="61" stroke="#333" marker-end="url(#m33)"/>
        <rect x="195" y="96" width="150" height="38" rx="7" fill="#fff7ea" stroke="#a06b1a"/>
        <text x="270" y="119" text-anchor="middle" font-size="10.5">불완전 순응 시 LATE</text>
        <line x1="270" y1="82" x2="270" y2="95" stroke="#333" marker-end="url(#m33)"/>
        <defs><marker id="m33" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#333"/></marker></defs>
      </svg>

      **그림 3.3.** 식별은 “알고리즘 선택”이 아니라 “질문+가정+표현”의 결합이다.

:::

      식별이 안 되는 경우에는 (i) 추가 자료 수집, (ii) 연구 설계 변경(무작위화/자연실험), (iii) 부분식별·민감도 분석으로
      질문을 재정의해야 한다.

      식별이 성립했다면 그 다음 단계는 표본에서 그 표현을 어떻게 계산할지의 문제다. 다음 절에서는 바로 그 추정 단계로 넘어간다.
