---
title: 1.2 반사실(counterfactual)의 정의와 직관적 예시
description: 1.1절은 데이터가 본질적으로 연상(association)의 언어만 제공한다는 점과, 인과 질문이 반사실(counterfactual)로 표현된다는 점을 강조했다. 이 절에서는 반사실을 잠재결과(potential outcomes)의 언어로 정의하고, 인과 추론의 근본 문제와 이를 다루는 직관·예시·가정의 뼈대를 단계적으로 정리한다.
---

# 1.2 반사실(counterfactual)의 정의와 직관적 예시

1.1절은 데이터가 본질적으로 **연상(association)**의 언어만 제공한다는 점과, 인과 질문이 **반사실(counterfactual)**로 표현된다는 점을 강조했다. 이 절에서는 반사실을 **잠재결과(potential outcomes)**의 언어로 정의하고, **인과 추론의 근본 문제**와 이를 다루는 직관·예시·가정의 뼈대를 단계적으로 정리한다.

    ## 1.2.0 원인의 결과와 결과의 원인 — Holland(1986)의 규범적 출발점

      이 절의 출발점은 단순한 “두 방향 비교”가 아니다. Holland(1986)의 핵심 주장은
      인과 분석은 전통적인 “결과의 원인(causes of effects)” 찾기보다
      **“원인의 결과(effects of causes)” 측정에서 시작해야 한다**는 규범적 명제다.
      즉 두 질문은 대등한 선택지가 아니라, 통계적 인과추론에서 우선순위가 다르다.

    \[
      \text{분석의 출발점: effects of causes} \;\;>\;\; causes of effects
    \]

:::

      그 이유는 명확하다. “결과의 원인”은 지식이 늘수록 계속 수정될 수 있는 설명 개념이지만,
      “원인의 결과”는 잠재결과 차이로 정밀하게 정의된다.

    \[
      \text{단위 }i\text{의 개인 인과효과: }\tau_i = Y_i(1)-Y_i(0)
    \]

:::

    ## 속성(attribute)과 원인(cause)의 구분

      Holland가 강조한 두 번째 축은 “원인”과 “속성”의 구분이다.
      성별·인종·출생연도 같은 속성은 같은 단위에 대해 조작 가능한 처치가 아니므로,
      잠재적으로 노출시킬 수 있는 처치(exposure)와 동일한 의미의 원인으로 다루기 어렵다.
      이것이 “NO CAUSATION WITHOUT MANIPULATION” 원칙의 핵심 맥락이다.

    \[
      \text{처치로 조작 가능한 변수 }T_i \text{는 인과효과 }Y_i(1)-Y_i(0)\text{를 정의할 수 있지만,}
    \]

:::

    \[
      \text{속성 }A_i\text{는 같은 단위에서 }A_i=a,\ a'\text{를 모두 실현시킬 수 없어 같은 방식의 잠재결과 비교가 어렵다.}
    \]

:::

    ## 근본 문제와 두 가지 해결 방향

      Holland의 근본 문제는 다음처럼 정확히 서술된다:
      같은 단위에서 \(Y_i(1)\)와 \(Y_i(0)\)를 동시에 관측할 수 없으므로 개인 효과
      \(\tau_i = Y_i(1)-Y_i(0)\)는 직접 관측 불가능하다.

    \[
      \text{Fundamental Problem:}\quad
      \text{cannot observe both }Y_i(1)\text{ and }Y_i(0)\text{ for the same unit }i.
    \]

:::

    Holland는 이 문제를 다루는 두 경로를 구분한다.

<table class="cf-table" role="table" aria-label="Holland의 근본 문제 해결 방향">
      <thead>
        <tr>
          <th scope="col">해결 방향</th>
          <th scope="col">핵심 아이디어</th>
          <th scope="col">핵심 가정</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>과학적 해결</td>
          <td>동일 단위 반복 노출 또는 동질 단위 비교</td>
          <td>동질성(homogeneity)·불변성(invariance)·시간 안정성</td>
        </tr>
        <tr>
          <td>통계적 해결</td>
          <td>개인 효과를 포기하고 평균 효과를 목표화</td>
          <td>무작위 배정 등으로 독립성 확보</td>
        </tr>
      </tbody>
    </table>

    \[
      \mathrm{ATE} = E\!\left[Y_i(1)-Y_i(0)\right] = E[Y_i(1)]-E[Y_i(0)]
    \]

:::

    ## Prima Facie 효과와 평균 인과효과의 구분

      관측된 처치군-통제군 평균 차이는 곧바로 평균 인과효과가 아니다.
      Holland는 이를 prima facie causal effect로 구분한다.

    \[
      T_{PF}=E\!\left[Y_i^{\mathrm{obs}}\mid T_i=1\right]-E\!\left[Y_i^{\mathrm{obs}}\mid T_i=0\right],\qquad
      \mathrm{ATE}=E[Y_i(1)]-E[Y_i(0)]
    \]

:::

    \[
      T_{PF}=\mathrm{ATE}+\left\{E[Y_i(0)\mid T_i=1]-E[Y_i(0)\mid T_i=0]\right\}
    \]

:::

      중괄호 항이 선택 편향이다. 무작위 배정 등으로 독립성이 성립할 때에만
      \(T_{PF}=\mathrm{ATE}\)가 된다. 따라서 인과 분석의 1차 과제는 “원인의 결과”를
      정밀하게 정의하고, 관측 차이를 그 정의와 연결하는 조건을 명시하는 것이다.


:::
summary

      핵심 정리 (Holland 관점)

        - “원인의 결과”는 “결과의 원인”과 대등한 선택지가 아니라, 통계적 인과분석의 우선 출발점이다.

        - 조작 가능성이 없는 속성은 Holland의 엄격한 의미에서 원인으로 취급하기 어렵다.

        - 근본 문제는 개인 효과의 직접 관측 불가능성이고, 과학적/통계적 해법으로 다뤄야 한다.

        - 관측 평균 차이 \(T_{PF}\)와 평균 인과효과 \(\mathrm{ATE}\)를 반드시 구분해야 하며, 그 차이는 선택 편향이다.

:::

      아래 1.2.1부터는 이 관점을 바탕으로 잠재결과 표기와 반사실 사고를 단계적으로 정리한다.

    ## 1.2.1 「만약 그랬다면」 — 인간 사고의 가장 자연스러운 형식

      인과적 사고는 일상에 깊게 박혀 있다. 우리는 끊임없이 반사실을 상상한다. 「그날 우산을 가져갔더라면 옷이 젖지 않았을 텐데.」 「그 약을 복용하지 않았더라면 부작용이 없었을 것이다.」 「최저임금을 올리지 않았더라면 고용률이 달랐을까?」 이 문장들은 공통 구조를 갖는다. 실제로 일어난 일(**사실**, factual)을 배경으로, 다르게 행동했더라면 결과가 어떻게 달라졌을지(**반사실**)를 상상하는 것이다.

      철학자 데이비드 루이스(David Lewis)는 1973년에 반사실 조건문을 **가능 세계(possible world)**의 언어로 형식화했다. 「만약 *X*였다면 *Y*였을 것이다」라는 문장의 진위는, 현실과 가장 가까운 가능 세계 가운데 *X*가 참인 세계에서 *Y*도 참인지를 묻는 방식으로 이해될 수 있다는 아이디어다. 이 철학적 직관은 통계학과 경제학에서 잠재결과라는 수학적 언어로 이어졌고, Pearl의 구조 인과 모형에서는 *do* 연산자와 반사실 변수로 다시 정련된다.

      아래에서는 반사실의 수학적 정의를 단계적으로 쌓되, 직관이 앞서가지 않도록 표기와 용어만 차분히 고정한다.

    ## 1.2.2 반사실의 수학적 정의 — 잠재결과의 언어

      반사실을 바로 다루는 표준 언어 가운데 하나가 **잠재결과 프레임워크(potential outcomes framework)**이다. 이 전개는 Neyman(1923)과 Rubin(1974)에 흔히 거슬러 올라가며, 오늘날 인과 추론 교과서에서 널리 쓰인다.

      **기본 설정.** 단위(unit) *i*는 분석 대상이 되는 개별 관측(사람·기업·국가 등)이다. 처치 *Ti*는 단위 *i*에 가해진 개입이고, 여기서는 이진(binary) 처치로 단순화하자. *Ti* = 1이면 처치를 받은 것, *Ti* = 0이면 받지 않은 것이다. 결과 변수 *Yi*는 관심 있는 측정값이다.

    잠재결과의 핵심 정의는 다음과 같다.

    \[
      Y_i(1) \equiv \text{단위 } i \text{가 처치를 받았을 때 }(T_i=1)\text{의 결과}, \quad
      Y_i(0) \equiv \text{단위 } i \text{가 처치를 받지 않았을 때 }(T_i=0)\text{의 결과}.
    \]

:::

      이 두 값은 단위 *i*에 대해 **동시에 정의**된다. 즉, 단위 *i*는 처치를 받든 받지 않든 각각의 결과를 「가지고 있다」고 가정한다. 잠재결과는 실제로 무엇이 일어났는지와 무관하게 정의되는 **반사실적 양(counterfactual quantities)**이다.

      이제 단위 *i*에 대한 **개인 인과효과(Individual Causal Effect, ICE)**를

    \[
      \tau_i \equiv Y_i(1) - Y_i(0)
    \]

:::

      로 둔다. 이것이 반사실을 수식에 옮긴 핵심이다. *τi*는 「같은 단위 *i*가 처치를 받았을 때의 결과」와 「같은 단위 *i*가 처치를 받지 않았을 때의 결과」의 차이다. 두 상태는 동시에 실현될 수 없다. 하나는 사실이 되고, 다른 하나는 반드시 반사실이 된다.

<svg width="440" height="200" viewBox="0 0 440 200" xmlns="http://www.w3.org/2000/svg">
        <text x="220" y="24" text-anchor="middle" font-size="12" fill="#1e4d6b" font-weight="700">한 단위 <tspan font-style="italic">i</tspan>에 대한 잠재결과 (개념도)</text>
        <rect x="40" y="50" width="140" height="56" rx="8" fill="#f5e8ec" stroke="#8b2942" stroke-width="1.5"/>
        <text x="110" y="80" text-anchor="middle" font-size="11" font-weight="600">Y<tspan baseline-shift="sub" font-size="9">i</tspan>(0)</text>
        <text x="110" y="96" text-anchor="middle" font-size="9" fill="#555">처치 없음</text>
        <rect x="260" y="50" width="140" height="56" rx="8" fill="#e8f5ef" stroke="#1d6b4a" stroke-width="1.5"/>
        <text x="330" y="80" text-anchor="middle" font-size="11" font-weight="600">Y<tspan baseline-shift="sub" font-size="9">i</tspan>(1)</text>
        <text x="330" y="96" text-anchor="middle" font-size="9" fill="#555">처치 있음</text>
        <text x="220" y="130" text-anchor="middle" font-size="13" fill="#333">ICE<tspan baseline-shift="sub" font-size="10">i</tspan> = Y<tspan baseline-shift="sub" font-size="9">i</tspan>(1) − Y<tspan baseline-shift="sub" font-size="9">i</tspan>(0)</text>
        <text x="220" y="158" text-anchor="middle" font-size="10" fill="#666">동시에 관측 불가 — 둘 중 하나만 실현</text>
        <line x1="190" y1="78" x2="250" y2="78" stroke="#999" stroke-width="1" stroke-dasharray="5 3"/>
        <text x="220" y="72" text-anchor="middle" font-size="9" fill="#888">차이</text>
      </svg>

      **그림 1.** 개인 인과효과(ICE)는 두 잠재결과의 차이다. 데이터에서는 한쪽만 본다.

:::

    ## 1.2.3 인과 추론의 근본 문제

      잠재결과 정의에서 바로 따라오는 사실이 있다. 우리는 *Yi*(1)과 *Yi*(0) 중 **하나만** 관측할 수 있다. 단위 *i*가 처치를 받았다면 *Yi*(1)은 관측되지만 *Yi*(0)은 관측되지 않는다. 그 반대도 마찬가지다. 관측 결과와 연결하면

    \[
      Y_i^{\mathrm{obs}} = T_i \, Y_i(1) + (1 - T_i) \, Y_i(0).
    \]

:::

      관측된 결과 *Yiobs*는 실제 처치 상태에 해당하는 잠재결과다. 나머지 한쪽, 즉 일어나지 않은 세계에서의 결과는 **근본적으로 관측 불가능**하다. Holland(1986)는 이를 **인과 추론의 근본 문제(Fundamental Problem of Causal Inference)**라고 불렀다.

      이것은 단순히 표본이 작아서가 아니다. 더 많은 데이터를 모은다고 해서, 동일한 단위·동일한 시점에서 두 잠재결과를 동시에 볼 수 있게 되지는 않는다. 인과 추론은 이 **근본적 결측(missingness)**을 어떤 가정 아래 보완할 것인가를 다루는 학문이라고도 볼 수 있다.

    아래 표는 한 집단에서 관측이 어떻게 「한 칸」만 남기는지를 보여준다.

<table class="cf-table" role="table" aria-label="잠재결과와 관측 가능성">
      <thead>
        <tr>
          <th scope="col">단위 <em>i</em></th>
          <th scope="col">처치 <em>T<sub>i</sub></em></th>
          <th scope="col"><em>Y<sub>i</sub></em>(1)</th>
          <th scope="col"><em>Y<sub>i</sub></em>(0)</th>
          <th scope="col">개인효과 <em>τ<sub>i</sub></em></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>1</td>
          <td><strong>관측됨</strong></td>
          <td>?</td>
          <td>?</td>
        </tr>
        <tr>
          <td>2</td>
          <td>0</td>
          <td>?</td>
          <td><strong>관측됨</strong></td>
          <td>?</td>
        </tr>
        <tr>
          <td>3</td>
          <td>1</td>
          <td><strong>관측됨</strong></td>
          <td>?</td>
          <td>?</td>
        </tr>
        <tr>
          <td>4</td>
          <td>0</td>
          <td>?</td>
          <td><strong>관측됨</strong></td>
          <td>?</td>
        </tr>
      </tbody>
    </table>

      물음표로 남은 칸이 곧 반사실이다. 이후 등장하는 모든 식별 전략은, 이 물음표를 어떤 가정 하에서 채울 것인가로 정리될 수 있다.

    ## 1.2.4 직관적 예시 ① — 아스피린과 두통

      철수가 두통으로 아스피린을 복용했고, 한 시간 뒤 두통이 가라앉았다고 하자. 철수는 「약이 듣었다」고 느낀다. 이것만으로 인과를 말할 수 있을까?

    \[\begin{aligned}
      Y_{\text{철수}}(1) &= \text{아스피린을 복용했을 때 한 시간 후 두통 강도},\\
      Y_{\text{철수}}(0) &= \text{아스피린을 복용하지 않았을 때 한 시간 후 두통 강도}.
    \end{aligned}\]

:::

      철수는 실제로 복용했으므로 우리가 보는 것은 *Y*철수(1)이다. 그러나 *Y*철수(0), 즉 「복용하지 않았더라면」의 두통 강도는 관측되지 않는다. 시간 경과만으로도 두통은 나아질 수 있고, 수분 섭취·휴식 등 다른 요인이 작용했을 수도 있다.

      철수의 경험은 *Y*철수(1)의 값을 알려 줄 뿐, 인과효과 *τ*철수 = *Y*철수(1) − *Y*철수(0)를 계산하려면 필요한 *Y*철수(0)은 영원히 관측되지 않는다. 이것이 개인 수준에서 인과 추론이 어려운 이유다.

      그렇다고 해서 아무것도 할 수 없는 것은 아니다. 한 가지 전형적인 방향은 개인 수준 *τi*를 포기하고, 집단 수준의 **평균 인과효과(Average Treatment Effect, ATE)**를 목표로 삼는 것이다.

    \[
      \mathrm{ATE} \equiv \mathbb{E}[\tau_i] = \mathbb{E}[Y_i(1) - Y_i(0)] = \mathbb{E}[Y_i(1)] - \mathbb{E}[Y_i(0)].
    \]

:::

      기댓값의 선형성 덕분에 ATE는 두 평균 잠재결과의 차로 쓸 수 있고, 문제는 이 두 평균을 데이터로부터 어떻게 **식별**할 것인가로 옮겨 간다.

    ## 1.2.5 직관적 예시 ② — 대학 교육의 임금 효과

      「대학 교육이 임금을 높이는가?」를 잠재결과로 쓰면 다음과 같다.

    \[\begin{aligned}
      Y_i(1) &= \text{개인 } i \text{가 대학에 진학했을 때의 임금},\\
      Y_i(0) &= \text{개인 } i \text{가 대학에 진학하지 않았을 때의 임금},\\
      \tau_i &= Y_i(1) - Y_i(0).
    \end{aligned}\]

:::

      데이터에서 대학 졸업자의 평균 임금이 고졸자보다 높다는 사실은 쉽게 확인된다. 그러나 그 차이가 곧 \(\mathbb{E}[Y_i(1)] - \mathbb{E}[Y_i(0)]\)의 추정인가? 그렇지 않다. 진학하는 사람과 하지 않는 사람은 처치 이전부터 능력·가정환경·동기 등에서 다를 수 있고, 이런 차이가 임금에도 영향을 준다면 단순 비교는 교육 효과와 **선택(selection)**이 뒤섞인 양이다.

    관측되는 단순 비교는 다음과 같이 분해된다.

    \[\begin{aligned}
      &\mathbb{E}[Y_i^{\mathrm{obs}} \mid T_i = 1] - \mathbb{E}[Y_i^{\mathrm{obs}} \mid T_i = 0] \\
      &\quad= \underbrace{\mathbb{E}[Y_i(1) \mid T_i = 1] - \mathbb{E}[Y_i(0) \mid T_i = 1]}_{\text{처치군에서의 평균 처치효과 (ATT)}} \\
      &\qquad+ \underbrace{\mathbb{E}[Y_i(0) \mid T_i = 1] - \mathbb{E}[Y_i(0) \mid T_i = 0]}_{\text{선택 편향 (selection bias)}}.
    \end{aligned}\]

:::

      두 번째 항이 선택 편향이다. 대학 진학자들이 진학하지 않았더라도(*Yi*(0) 기준으로) 원래 고졸 집단보다 임금이 높았을 사람들이라면, 단순 비교는 교육의 효과를 과대추정할 수 있다. 인과 추론의 핵심 과제는 이 편향을 제거하거나, 그 크기를 드러내는 가정을 정당화하는 것이다.

    ## 1.2.6 직관적 예시 ③ — 클로드 베르나르의 실험과 반사실

      19세기 프랑스 생리학자 클로드 베르나르(Claude Bernard)는 쿠라레(curare)가 근육을 마비시키는 메커니즘을 연구하면서, 개구리에게 쿠라레를 투여했을 때 운동은 마비되나 감각은 유지된다는 관측을 했다. 이것이 인과인지, 단순히 함께 나타나는 패턴인지를 가리려면 어떤 비교가 필요한가?

      베르나르가 비교한 것은, 같은 종류의 개구리를 놓고 **쿠라레를 투여한 경우**와 **투여하지 않은 경우**를 나란히 두는 실험 설계다. 한 마리에게 동시에 두 조건을 줄 수 없다는 점에서, 우리는 다시 한 번 근본 문제에 부딪힌다. 베르나르가 쓴 해법의 한 형태는 **집단 수준의 무작위 배정**에 가깝다. 여러 개구리를 처치군과 통제군에 무작위로 나누면, 잠재결과의 평균이 집단 간에 대등해지도록 비교를 설계할 수 있다는 논리다. 이것이 현대 무작위 대조 시험(RCT)이 지닌 직관의 역사적 한 단면이다.

      실험은 관측 불가능한 반사실을 「직접 보여 주는」 장치가 아니라, 집단 수준에서 반사실을 **대리(proxy)**하는 비교 집단을 구성하는 장치다.

<svg width="460" height="180" viewBox="0 0 460 180" xmlns="http://www.w3.org/2000/svg">
        <text x="230" y="22" text-anchor="middle" font-size="12" fill="#1e4d6b" font-weight="700">실제 세계의 한 경로만 관측</text>
        <circle cx="100" cy="100" r="18" fill="#fff" stroke="#333" stroke-width="2"/>
        <text x="100" y="105" text-anchor="middle" font-size="11">시작</text>
        <line x1="118" y1="100" x2="200" y2="100" stroke="#333" stroke-width="2" marker-end="url(#mcf)"/>
        <defs>
          <marker id="mcf" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><polygon points="0 0, 8 4, 0 8" fill="#333"/></marker>
        </defs>
        <rect x="200" y="78" width="80" height="44" rx="6" fill="#e8f5ef" stroke="#1d6b4a"/>
        <text x="240" y="105" text-anchor="middle" font-size="10"><tspan font-style="italic">T</tspan>=1 선택</text>
        <line x1="280" y1="100" x2="360" y2="100" stroke="#333" stroke-width="2" marker-end="url(#mcf)"/>
        <rect x="360" y="78" width="80" height="44" rx="6" fill="#e8f0f5" stroke="#1e4d6b"/>
        <text x="400" y="105" text-anchor="middle" font-size="10"><tspan font-style="italic">Y</tspan> 관측</text>
        <text x="230" y="150" text-anchor="middle" font-size="10" fill="#666">반대 분기 <tspan font-style="italic">T</tspan>=0에서의 <tspan font-style="italic">Y</tspan>(0)는 같은 실험에서 볼 수 없음</text>
      </svg>

      **그림 2.** 한 단위의 「역사」는 하나의 처치 분기만 밟는다. 반대 분기의 잠재결과는 반사실로 남는다.

:::

    ## 1.2.7 반사실의 세 가지 층위 — Pearl의 인과 사다리

      Pearl(2000, 2018)은 인과적 사고를 세 층위로 나누는 **인과 사다리(ladder of causation)**를 제안했다. 반사실이 전체 지형도에서 어디에 놓이는지를 보여 주는 틀이다(다음 절 1.3에서 더 체계적으로 이어진다).

    **1층: 연상(Association)** — \(P(Y \mid X)\). 관측 데이터에서 변수 간 통계적 패턴을 읽는 층위다. 예측·기계학습·표준 회귀의 상당 부분이 이 층위에서 작동한다.

    **2층: 개입(Intervention)** — \(P(Y \mid \mathrm{do}(X))\). 실제로 \(X\)를 조작했을 때의 결과를 묻는 층위다. Pearl의 \(\mathrm{do}\) 연산자가 이를 형식화한다. 무작위 실험은 이 층위의 질문에 정면으로 답하도록 설계되는 경우가 많다.

    **3층: 반사실(Counterfactual)** — \(P(Y_x \mid X=x',\, Y=y')\)와 같은 언어로 표현되는, 이미 관측된 사실을 전제로 한 「다른 행동이었다면」의 질문이다. 법적 책임, 의학적 귀인, 개인 맞춤 의사결정이 이 층위를 요구한다.

      상위 층위는 하위 층위에 정보를 포함하는 방향으로 이해할 수 있다. 반사실을 일관되게 다룰 수 있으면 개입·연상에 대한 질문도 정리할 수 있는 경우가 많고, 개입 수준의 양을 알면 연상은 따라온다. 그러나 **역방향은 성립하지 않는다**. 연상만으로 개입이나 반사실에 답할 수 없다는 점이, 회귀만으로는 인과 질문이 부족한 이유와 맞닿아 있다.

    \[
      \text{반사실} \;\supset\; \text{개입} \;\supset\; \text{연상}
    \]

:::

    ## 1.2.8 반사실의 식별 — 어떤 가정이 필요한가

      처치를 받은 단위 *i*에 대해 「받지 않았더라면」의 결과 *Yi*(0)은 원칙적으로 관측되지 않는다. 그렇다면 반사실에 대해 과학적 주장을 어떻게 할 수 있는가? 답은 **가정(assumption)**이다. 특정 가정이 성립할 때, 관측 가능한 통계량이 관심 있는 반사실적 양과 일치한다는 논증을 세울 수 있다.

      가장 단순한 예는 무작위 배정이다. 처치가 무작위로 배정되면

    \[
      \{Y_i(1), Y_i(0)\} \perp\!\!\!\perp T_i
    \]

:::

      가 성립한다고 가정할 수 있다. 즉, 잠재결과가 처치 배정과 독립이다. 이 조건 아래에서는

    \[\begin{aligned}
      \mathbb{E}[Y_i(1)] &= \mathbb{E}[Y_i(1) \mid T_i = 1] = \mathbb{E}[Y_i^{\mathrm{obs}} \mid T_i = 1],\\
      \mathbb{E}[Y_i(0)] &= \mathbb{E}[Y_i(0) \mid T_i = 0] = \mathbb{E}[Y_i^{\mathrm{obs}} \mid T_i = 0]
    \end{aligned}\]

:::

      와 같이 평균 잠재결과가 대응하는 처치군·통제군의 표본 평균으로 바뀐다. 따라서 평균의 차(difference in means)가 ATE에 대한 비편향 추정량이 된다.

    \[
      \mathrm{ATE} = \mathbb{E}[Y_i(1)] - \mathbb{E}[Y_i(0)]
      = \mathbb{E}[Y_i^{\mathrm{obs}} \mid T_i = 1] - \mathbb{E}[Y_i^{\mathrm{obs}} \mid T_i = 0].
    \]

:::

      무작위 실험이 「황금 기준」으로 불리는 이유 가운데 하나가, 강한 가정 하나로 관측 불가능한 반사실적 평균을 관측 가능한 비교로 바꿀 수 있다는 점이다. 이 책 후반의 도구변수·RDD·DiD·매칭 등은 무작위 배정이 없을 때, 다른 가정으로 그 대체 논리를 확보하려는 시도로 읽을 수 있다.

    ## 1.2.9 반사실과 도덕적·법적 귀인

      반사실적 사고는 과학을 넘어 법과 도덕에서도 중심축을 이룬다. 법철학에서 널리 쓰이는 **「but-for」 기준**이 그 예다. 「피고의 행위가 없었더라면(but for the defendant’s action) 피해가 발생했을 것인가?」는 반사실적 질문이다.

      의약품 부작용 소송을 떠올려 보자. 환자가 약을 복용한 뒤 심장 발작을 겪었다면, 약이 원인인지 판단하려면 「같은 환자가 그 약을 복용하지 않았더라면」이라는 반사실에 답해야 한다. 그러나 그 반사실은 관측되지 않는다. 법원은 역학 연구·임상시험·전문가 증언 등을 통해 이를 간접적으로 추론한다. 이 과정에서 인과 추론의 방법론이 실제 제도와 맞물린다.

      반사실은 학술 용어에 머무르지 않고, 책임을 귀속하고 정책을 평가하며 개인의 결정을 내리는 사고의 틀 그 자체다.


:::
summary

      핵심 요약

        - 반사실(counterfactual)은 실제로 일어난 일을 전제로 「다르게 행동했더라면 어떤 결과였을까」를 묻는 사고이며, 잠재결과 *Yi*(1), *Yi*(0)로 수학화한다.

        - 개인 인과효과 *τi* = *Yi*(1) − *Yi*(0)에서 한쪽 잠재결과는 항상 관측되지 않는다. 이것이 **인과 추론의 근본 문제**다.

        - 인과 추론은 이 관측 불가능성을 무작위 배정, 조건부 독립, 연속성 등 **특정 가정**으로 보완하는 학문이다.

        - Pearl의 인과 사다리는 연상 → 개입 → 반사실의 셋으로 사고를 나누며, 상위 층위가 하위 층위로 환원되지는 않는다. 회귀는 연상 층위의 도구로 이해될 수 있고, 인과 질문은 그보다 높은 층위를 요구한다.

        - 무작위 배정은 \(\{Y_i(1), Y_i(0)\} \perp\!\!\!\perp T_i\)를 통해 평균 잠재결과를 처치군·통제군의 관측 평균으로 연결해, 반사실적 평균을 관측 가능한 비교로 대체한다.

:::

      다음 절([1.3 인과 질문의 세 층위 — Pearl의 인과 사다리](ch01-03-ladder.html))에서는 인과 사다리를 한층 체계적으로 정리하고, 세 층위의 질문이 각각 어떤 수학적 언어(구조 인과 모형과 \(\mathrm{do}\) 연산자 등)를 요구하는지로 이어간다.
