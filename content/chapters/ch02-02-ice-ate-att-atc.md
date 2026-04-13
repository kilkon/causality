---
title: 2.2 개인 인과효과와 평균 인과효과 — ICE · ATE · ATT · ATC
description: 잠재결과를 정의한 뒤에는 효과를 어떤 수준에서 요약할지 정해야 한다. 이 절은 개인 인과효과와 평균 인과효과의 관계를 정리하고, 왜 질문에 따라 목표 모수가 달라지는지를 설명한다.
---

# 2.2 개인 인과효과와 평균 인과효과 — ICE · ATE · ATT · ATC

2.1절에서 단위, 처치, 잠재결과를 정의했다면 이제 자연스럽게 다음 질문이 따라온다. “그래서 효과를 무엇으로 정의할 것인가?” 이 질문은 단순해 보이지만, 실제로는 인과추론의 목표 모수를 정하는 핵심 단계다. 같은 연구라도 개인 효과를 묻는지, 전체 평균효과를 묻는지, 처치받은 집단에 대한 효과를 묻는지에 따라 해석과 추정 전략이 달라진다.

## 2.2 개인 인과효과와 평균 인과효과 — ICE · ATE · ATT · ATC
    ## 2.2.1 왜 효과를 구분해서 정의해야 하는가

      잠재결과 \(Y_i(1)\), \(Y_i(0)\)을 정의한 뒤의 질문은 곧바로 「효과를 어떻게 정의할 것인가」로 옮겨 간다. 여기서 효과는 하나의 값이 아니라 여러 수학적 대상(ICE, ATE, ATT, ATC, CATE, LATE)으로 갈라진다. 누구를 기준 집단으로 평균하는지, 어떤 척도로 읽는지에 따라 해석이 달라지기 때문이다.

      정책 질문(보편 확대)과 임상 질문(이 환자에게 효과가 있었는가)은 같은 듯 보이지만 목표 모수가 다르다. 전자는 ATE·ATC에 가깝고, 후자는 개인 반사실 또는 그 근사에 가깝다. 아래에서는 각 효과를 분리 정의하고, 해석·식별·상호 관계를 정리한다.

    ## 2.2.2 개인 인과효과(ICE)
    **정의.**

    \[
      \tau_i \equiv Y_i(1) - Y_i(0)
    \]

:::

      다음 절에서는 이렇게 정의된 효과가 실제로 관측 데이터와 연결되기 위해 어떤 안정성 조건이 필요한지, 즉 SUTVA와 결측 데이터 관점을 통해 잠재결과 프레임워크의 핵심 가정을 정리한다.

      이는 동일 단위 \(i\)의 두 잠재결과 차이이며, 둘 중 하나는 반드시 반사실이다. 따라서 ICE는 원칙적으로 직접 관측되지 않는다.

    **이질성.** 일반적으로 \(\tau_i \neq \tau_j\)이며, 이것이 처치 효과 이질성이다. 원천은 관측 가능한 \(\mathbf{X}_i\) 기반 이질성과 관측 불가능한 \(U_i\) 기반 이질성으로 나눠 볼 수 있다.

    **관측 가능성의 수식.**

    \[
      Y_i^{\mathrm{obs}} =
      \begin{cases}
        Y_i(1) & \text{if } D_i = 1, \\
        Y_i(0) & \text{if } D_i = 0.
      \end{cases}
    \]

:::

<table class="po-table" aria-label="ICE 관측 불가능성 예시">
      <thead>
        <tr><th>단위 \(i\)</th><th>\(D_i\)</th><th>\(Y_i(1)\)</th><th>\(Y_i(0)\)</th><th>\(\tau_i\)</th></tr>
      </thead>
      <tbody>
        <tr><td>1</td><td>1</td><td><strong>8</strong></td><td>?</td><td>?</td></tr>
        <tr><td>2</td><td>1</td><td><strong>5</strong></td><td>?</td><td>?</td></tr>
        <tr><td>3</td><td>0</td><td>?</td><td><strong>4</strong></td><td>?</td></tr>
        <tr><td>4</td><td>0</td><td>?</td><td><strong>7</strong></td><td>?</td></tr>
        <tr><td>5</td><td>1</td><td><strong>9</strong></td><td>?</td><td>?</td></tr>
        <tr><td>6</td><td>0</td><td>?</td><td><strong>3</strong></td><td>?</td></tr>
      </tbody>
    </table>

      특수한 구조 가정(예: 강한 동질성 \(\tau_i=\tau\)) 하에서는 개인 효과를 평균 효과와 가깝게 다룰 수 있지만, 일반적 가정은 아니다.

    ## 2.2.3 평균 인과효과(ATE)
    \[
      \mathrm{ATE} \equiv \mathbb{E}[\tau_i] = \mathbb{E}[Y_i(1)-Y_i(0)] = \mathbb{E}[Y_i(1)]-\mathbb{E}[Y_i(0)].
    \]

:::

      ATE는 전체 모집단에 대한 평균 효과다. 보편 정책의 평균 효과를 묻는 질문에 자연스럽다.

    **무작위 배정 하 식별.** \(\{Y_i(1),Y_i(0)\}\perp\!\!\!\perp D_i\)이면

    \[
      \mathrm{ATE}
      = \mathbb{E}[Y_i^{\mathrm{obs}} \mid D_i=1]
      - \mathbb{E}[Y_i^{\mathrm{obs}} \mid D_i=0].
    \]

:::

    즉 처치군-통제군의 평균 차이가 ATE의 비편향 추정량이 된다.

    ## 2.2.4 처치군 평균 인과효과(ATT)
    \[
      \mathrm{ATT}
      \equiv \mathbb{E}[\tau_i \mid D_i=1]
      = \mathbb{E}[Y_i(1)\mid D_i=1] - \mathbb{E}[Y_i(0)\mid D_i=1].
    \]

:::

      ATT는 실제 처치군에서의 평균 효과다. 프로그램 유지·성과 평가처럼 「현재 참여자에게 효과가 있었는가」를 묻는 맥락에 맞다.

    **관측 차이의 분해.**

    \[
      \underbrace{\mathbb{E}[Y_i^{\mathrm{obs}}\mid D_i=1]-\mathbb{E}[Y_i^{\mathrm{obs}}\mid D_i=0]}_{\text{관측 평균 차이}}
      =
      \underbrace{\mathrm{ATT}}_{\text{처치군 효과}}
      +
      \underbrace{\mathbb{E}[Y_i(0)\mid D_i=1]-\mathbb{E}[Y_i(0)\mid D_i=0]}_{\text{선택 편향}}.
    \]

:::

    관측 연구가 어려운 핵심은 마지막 선택 편향 항을 직접 볼 수 없다는 점이다.

    ## 2.2.5 통제군 평균 인과효과(ATC)
    \[
      \mathrm{ATC}
      \equiv \mathbb{E}[\tau_i \mid D_i=0]
      = \mathbb{E}[Y_i(1)\mid D_i=0] - \mathbb{E}[Y_i(0)\mid D_i=0].
    \]

:::

      ATC는 현재 통제군(비참여자)에게 처치를 확대했을 때의 평균 효과다. 정책 확장(scale-up) 평가에서 중요하다.

    ## 2.2.6 세 추정량의 관계
    처치 비율 \(\pi \equiv P(D_i=1)\)일 때

    \[
      \mathrm{ATE} = \pi\cdot \mathrm{ATT} + (1-\pi)\cdot \mathrm{ATC}.
    \]

:::

    또한 \(\{Y_i(1),Y_i(0)\}\perp\!\!\!\perp D_i\)이면 \(\mathrm{ATE}=\mathrm{ATT}=\mathrm{ATC}\)가 성립한다.

    **수치 예시.** 아래 완전 잠재결과(설명용)에서는 ATT가 가장 크고 ATC가 가장 작다.

<table class="po-table" aria-label="ATE ATT ATC 수치 예시">
      <thead>
        <tr><th>단위 \(i\)</th><th>\(D_i\)</th><th>\(Y_i(1)\)</th><th>\(Y_i(0)\)</th><th>\(\tau_i\)</th></tr>
      </thead>
      <tbody>
        <tr><td>1</td><td>1</td><td>8</td><td>4</td><td><strong>4</strong></td></tr>
        <tr><td>2</td><td>1</td><td>5</td><td>2</td><td><strong>3</strong></td></tr>
        <tr><td>3</td><td>1</td><td>9</td><td>5</td><td><strong>4</strong></td></tr>
        <tr><td>4</td><td>0</td><td>6</td><td>5</td><td><strong>1</strong></td></tr>
        <tr><td>5</td><td>0</td><td>4</td><td>4</td><td><strong>0</strong></td></tr>
        <tr><td>6</td><td>0</td><td>5</td><td>3</td><td><strong>2</strong></td></tr>
      </tbody>
    </table>

    \[
      \mathrm{ATE}=\frac{14}{6}\approx 2.33,\quad
      \mathrm{ATT}=\frac{11}{3}\approx 3.67,\quad
      \mathrm{ATC}=1.00.
    \]

:::

    \[
      \mathbb{E}[Y^{\mathrm{obs}}\mid D=1]-\mathbb{E}[Y^{\mathrm{obs}}\mid D=0]
      = \frac{10}{3}\approx 3.33
      = \underbrace{3.67}_{\mathrm{ATT}} + \underbrace{(-0.33)}_{\text{선택 편향}}.
    \]

:::

    ## 2.2.7 CATE(조건부 평균 처치효과)
    \[
      \tau(\mathbf{x}) \equiv \mathbb{E}[\tau_i \mid \mathbf{X}_i=\mathbf{x}]
      = \mathbb{E}[Y_i(1)-Y_i(0)\mid \mathbf{X}_i=\mathbf{x}].
    \]

:::

    CATE는 이질성 구조를 \(\mathbf{X}\)의 함수로 나타낸다. ATE·ATT·ATC는 CATE를 서로 다른 분포로 주변화한 값이다.

    \[
      \mathrm{ATE}=\int \tau(\mathbf{x})\,dP(\mathbf{x}),\quad
      \mathrm{ATT}=\int \tau(\mathbf{x})\,dP(\mathbf{x}\mid D=1),\quad
      \mathrm{ATC}=\int \tau(\mathbf{x})\,dP(\mathbf{x}\mid D=0).
    \]

:::

    최적 처치 규칙의 기본형은 \(d^*(\mathbf{x})=\mathbb{1}[\tau(\mathbf{x})>0]\)처럼 쓸 수 있다.

    ## 2.2.8 효과 척도: 차이 vs 비율
    \[
      \mathrm{RD}=P(Y_i(1)=1)-P(Y_i(0)=1),\quad
      \mathrm{RR}=\frac{P(Y_i(1)=1)}{P(Y_i(0)=1)},
    \]

:::

    \[
      \mathrm{OR}=
      \frac{P(Y_i(1)=1)/P(Y_i(1)=0)}{P(Y_i(0)=1)/P(Y_i(0)=0)}.
    \]

:::

    효과 수정(effect modification)은 척도 의존적일 수 있으므로, 결과 보고 시 선택한 척도를 명시해야 한다.

    ## 2.2.9 LATE(국소 평균 처치효과)

      IV 맥락에서는 순응자(compliers) 부분 모집단의 평균 효과인 LATE(Imbens &amp; Angrist, 1994)를 쓴다.

    \[
      \mathrm{LATE} \equiv \mathbb{E}[\tau_i \mid \text{complier}].
    \]

:::

    LATE는 ATE/ATT/ATC와 다른 목표 모수이며, 외부 타당도 해석을 별도로 요구한다.

    ## 2.2.10 효과 측도의 통합 지도
    \[
      \underbrace{\tau_i = Y_i(1)-Y_i(0)}_{\text{ICE}}
      \;\rightarrow\;
      \underbrace{\tau(\mathbf{x})=\mathbb{E}[\tau_i\mid \mathbf{X}_i=\mathbf{x}]}_{\text{CATE}}
      \;\rightarrow\;
      \begin{cases}
        \mathrm{ATE}=\int \tau(\mathbf{x})\,dP(\mathbf{x}) \\
        \mathrm{ATT}=\int \tau(\mathbf{x})\,dP(\mathbf{x}\mid D=1) \\
        \mathrm{ATC}=\int \tau(\mathbf{x})\,dP(\mathbf{x}\mid D=0)
      \end{cases}
    \]

:::

    연구 질문이 무엇인지(보편 정책, 현재 참여자 평가, 정책 확대, 개인화 의사결정)를 먼저 정해야 목표 모수와 추정 전략이 정해진다.


:::
summary

      2.2 핵심 요약

        - ICE \(\tau_i=Y_i(1)-Y_i(0)\)는 개인 수준 효과지만 직접 관측 불가능하다.

        - ATE는 전체 평균, ATT는 처치군 평균, ATC는 통제군 평균 효과를 뜻한다.

        - 세 추정량은 \(\mathrm{ATE}=\pi\mathrm{ATT}+(1-\pi)\mathrm{ATC}\) 관계로 연결된다.

        - 관측 평균 차이는 ATT와 선택 편향의 합으로 분해된다.

        - CATE는 이질성의 구조를 보여 주며, ATE·ATT·ATC는 CATE의 주변화다.

:::
