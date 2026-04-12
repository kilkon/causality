---
title: 1.3 인과 사다리와 구조 인과 모형 — 세 층위의 형식화
description: 1.2절에서 반사실은 관측 데이터만으로는 직접 말해 주지 않는다는 점을 잠재결과의 언어로 정리했다. Pearl은 이를 2000년 Causality에서 이론적으로 제시하고, 2018년 The Book of Why에서 인과 사다리라는 이름으로 널리 소개했다. 핵심은 간단하다. 인과 질문은 층위가 다르고, 낮은 층위의 언어만으로는 높은 층위의 질문에 원칙적으로 답할 수 없다. 이 절은 그 위계를 SCM과 \(\mathrm{do}\) 연산자의 문법으로 정리한다.
---

# 1.3 인과 사다리와 구조 인과 모형 — 세 층위의 형식화

1.2절에서 반사실은 관측 데이터만으로는 직접 말해 주지 않는다는 점을 잠재결과의 언어로 정리했다. Pearl은 이를 2000년 *Causality*에서 이론적으로 제시하고, 2018년 *The Book of Why*에서 인과 사다리라는 이름으로 널리 소개했다. 핵심은 간단하다. 인과 질문은 층위가 다르고, 낮은 층위의 언어만으로는 높은 층위의 질문에 원칙적으로 답할 수 없다. 이 절은 그 위계를 SCM과 \(\mathrm{do}\) 연산자의 문법으로 정리한다.

## 1.3.1 왜 층위를 구분해야 하는가

Pearl(2000, 2009, 2018)이 강조한 핵심은 인과적 질문이 하나가 아니라는 점이다. 같은 데이터라도 우리가 묻는 질문이

- 단지 함께 나타나는 패턴을 알고 싶은 것인지,
- 개입했을 때 무슨 일이 일어나는지 알고 싶은 것인지,
- 실제로는 다른 선택을 했는데 만약 달리 행동했더라면 어땠을지를 묻는 것인지

에 따라 필요한 정보의 수준이 달라진다. Pearl은 이 서로 다른 질문의 종류를 **인과 사다리(ladder of causation)**라는 위계로 설명했다.

여기서 매우 중요한 점이 하나 있다. **사다리의 층은 do-operator와 counterfactual 같은 표기 자체가 아니라, 질의(query)의 종류**라는 것이다. 다시 말해 Pearl이 계층적으로 놓은 것은

1. 연관(association)
2. 개입(intervention)
3. 반사실(counterfactual)

의 세 층위다. 이때 \(\mathrm{do}(\cdot)\)는 2층인 개입을 형식화하는 수학적 연산자이지, 2층과 나란히 놓인 별도의 철학적 범주가 아니다. 반사실은 오히려 이 개입 개념을 포함해 더 복합적인 비교를 수행하는 상위 질의다.

이 절에서는 세 층위를 소개하고, 각 층위를 형식화하는 언어가 무엇인지 구분한 뒤, SCM이 이 층위들을 하나의 틀 안에서 어떻게 연결하는지 본다.

## 1.3.2 인과 사다리의 세 층위 — 질의의 위계

Pearl의 사다리를 가장 정확하게 이해하는 방법은 “세 개의 다른 질문층”으로 읽는 것이다. 먼저 표로 직관을 고정해 보자.

<table class="ladder-table" role="table" aria-label="인과 사다리 세 층위">
      <thead>
        <tr>
          <th scope="col">층위</th>
          <th scope="col">이름</th>
          <th scope="col">핵심 동사</th>
          <th scope="col">핵심 질문</th>
          <th scope="col">수학적 표현</th>
          <th scope="col">주체/도구</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1층</td>
          <td>연관(Association)</td>
          <td>보다(See)</td>
          <td>관측했을 때 무엇을 보는가?</td>
          <td>\(P(Y \mid X)\)</td>
          <td>동물·통계·ML</td>
        </tr>
        <tr>
          <td>2층</td>
          <td>개입(Intervention)</td>
          <td>하다(Do)</td>
          <td>행동했을 때 무슨 일이 일어나는가?</td>
          <td>\(P(Y \mid \mathrm{do}(X))\)</td>
          <td>도구 사용자·실험자</td>
        </tr>
        <tr>
          <td>3층</td>
          <td>반사실(Counterfactual)</td>
          <td>상상하다(Imagine)</td>
          <td>달리 행동했더라면 어떻게 되었을까?</td>
          <td>\(P(Y_x \mid X = x',\, Y = y')\)</td>
          <td>인간·SCM</td>
        </tr>
      </tbody>
    </table>

세 층위는 정보량의 위계를 이룬다. 3층 질문에 답할 수 있는 모델은 2층·1층 질문에도 답할 수 있는 경우가 많다. 그러나 **역은 성립하지 않는다**. 관측 데이터는 대체로 1층의 언어로 주어지지만, 정책평가에서 알고 싶은 것은 대개 2층이나 3층이다. 이 비대칭이 인과추론을 어렵게 만드는 한 원인이다.

Pearl은 이 구분을 인지 능력의 위계로도 설명한다. 패턴 인식은 1층, 계획적 개입은 2층, 반사실적 상상과 책임 귀속은 3층에 대응한다는 해석이다.

<svg width="420" height="280" viewBox="0 0 420 280" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="lg13" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#e8f0f5"/>
            <stop offset="100%" style="stop-color:#f0ebe3"/>
          </linearGradient>
        </defs>
        <text x="210" y="28" text-anchor="middle" font-size="13" fill="#1e4d6b" font-weight="700">Pearl의 인과 사다리 (개념도)</text>
        <rect x="60" y="48" width="300" height="200" rx="8" fill="url(#lg13)" stroke="#b8c9d4"/>
        <rect x="90" y="68" width="240" height="48" rx="6" fill="#fff" stroke="#6b4c9a" stroke-width="2"/>
        <text x="210" y="88" text-anchor="middle" font-size="11" font-weight="700" fill="#4a3569">3. 반사실 (Counterfactuals)</text>
        <text x="210" y="106" text-anchor="middle" font-size="9" fill="#555">「이미 일어난 일」에 대한 「만약」 — 개별 역사</text>
        <rect x="90" y="132" width="240" height="48" rx="6" fill="#fff" stroke="#1d6b4a" stroke-width="2"/>
        <text x="210" y="152" text-anchor="middle" font-size="11" font-weight="700" fill="#145a3a">2. 개입 (Intervention)</text>
        <text x="210" y="170" text-anchor="middle" font-size="9" fill="#555">do(X), 정책·처치를 집단에 적용</text>
        <rect x="90" y="196" width="240" height="48" rx="6" fill="#fff" stroke="#1e4d6b" stroke-width="2"/>
        <text x="210" y="216" text-anchor="middle" font-size="11" font-weight="700" fill="#1e4d6b">1. 연관 (Association)</text>
        <text x="210" y="234" text-anchor="middle" font-size="9" fill="#555">P(Y|X) — 관측 데이터에서의 조건부 분포</text>
        <text x="210" y="262" text-anchor="middle" font-size="13" fill="#666">↑ 위로 갈수록 강한 가정 · 더 많은 구조 정보 필요</text>
      </svg>

      **그림 1.** 하위 층의 통계만으로 상위 층의 답을 얻을 수 없다. SCM·식별 가정이 층 사이의 다리가 된다.


## 1.3.3 1층: 연관(Association) — \(P(Y \mid X)\)

**직관.** 연관의 층위는 관측 데이터 안에서의 패턴을 묻는다. “\(X\)를 보았을 때 \(Y\)에 대해 무엇을 알 수 있는가?”가 이 층의 질문이다. 인과 구조를 명시하지 않아도, 두 변수가 함께 어떻게 분포하는지는 기술할 수 있다.

      - 아스피린을 복용한 사람들의 두통 완화율은 얼마인가?

      - 대학 졸업자의 평균 임금은 고졸자보다 얼마나 높은가?

      - 흡연자의 폐암 발생률은 비흡연자보다 얼마나 높은가?

    이런 질문은 \(P(Y \mid X=x)\)의 형태로 쓸 수 있고, 데이터에서 추정하는 데 인과 구조 가정이 필수는 아니다.

    **수식.** 연관은 결합분포 \(P(X,Y)\)에서 파생된 조건부 분포다.

    \[
      P(Y = y \mid X = x) = \frac{P(Y = y,\, X = x)}{P(X = x)}.
    \]



회귀, 기계학습, 상관, 조건부 기댓값 \(\mathbb{E}[Y \mid X=x]\)는 모두 이 층위의 도구다. 그러나 이들만으로 “세계를 이렇게 바꾸면 무엇이 일어나는가”에 답하는 것은 원칙적으로 불가능하다.

**한계.** \(P(Y \mid X=x)\)는 DGP에 의존한다. 같은 표면적 데이터라도 생성 구조가 다르면 개입의 결과는 달라질 수 있다. 아이스크림 판매(\(X\))와 익사 사고(\(Y\))의 조건부 분포를 아무리 정밀히 맞춰도, 아이스크림 판매를 금지했을 때 익사가 줄어드는지는 \(P(Y \mid X)\)만으로는 읽히지 않는다. \(P(Y \mid X)\)는 \(P(Y \mid \mathrm{do}(X))\)에 대해 침묵한다.

## 1.3.4 2층: 개입(Intervention) — \(P(Y \mid \mathrm{do}(X))\)

**직관.** 개입의 층위는 세계에 외부에서 개입했을 때의 결과를 묻는다. “만약 내가 \(X\)를 \(x\)로 **강제로** 설정한다면, \(Y\)는 어떻게 분포하는가?”가 이 층의 질문이다. 단순 관측이 아니라 조작(manipulation)을 상상한다.

      - 모든 환자에게 아스피린을 투여한다면 두통 완화율은?

      - 정부가 최저임금을 인상한다면 고용률은?

      - 플랫폼에서 추천 알고리즘을 끈다면 체류 시간은?

\(P(Y \mid X=x)\)는 “자연적으로 \(X=x\)인 집단을 관측했을 때”이고, \(P(Y \mid \mathrm{do}(X=x))\)는 “외부에서 \(X=x\)로 설정했을 때”다. 둘이 달라지는 대표적 경우가 \(X\)와 \(Y\) 사이에 **교란(confounding)**이 있을 때다.

여기서 강조할 점이 바로 \(\mathrm{do}\)의 지위다. Pearl의 사다리에서 2층의 항목은 **do-operator 자체가 아니라 intervention이라는 질의 범주**다. \(\mathrm{do}(X=x)\)는 그 intervention을 수학적으로 표현하는 연산자다. 따라서 “do-operator와 counterfactual이 나란한 두 층이다”라고 이해하면 부정확하다. 더 정확히는, **개입 층을 표현하는 도구가 do-operator**라고 해야 한다.

**\(\mathrm{do}\) 연산자.** Pearl은 개입을 \(\mathrm{do}(\cdot)\)로 형식화했다. \(\mathrm{do}(X=x)\)는 \(X\)를 값 \(x\)로 강제 설정하는 조작이다. SCM을 도입하면 이 조작은 **그래프 절단(graph surgery)**으로 해석된다(§1.3.8).

    \[
      P(Y = y \mid X = x) \quad \text{vs.} \quad P(Y = y \mid \mathrm{do}(X = x)).
    \]



    교란이 없을 때(예: 무작위 실험) 둘은 같아질 수 있다. 교란이 있으면 일반적으로 다르다.

**성질(요약).** \(\mathrm{do}\)는 변수 집합에도 적용된다. \(\mathrm{do}(X=x,\, Z=z)\)는 동시 개입이다. 개입의 중첩은 일상적인 의미의 조건화와 혼동하기 쉬우나, \(\mathrm{do}\)와 관측 조건화는 일반적으로 **교환 가능하지 않다**.

또 하나 중요한 점은, Pearl 자신도 개입과 반사실 모두를 \(\mathrm{do}(x)\)를 통해 의미론적으로 정리한다는 것이다. 즉 \(\mathrm{do}\)는 2층을 정의할 뿐 아니라, 3층 반사실을 구성하는 하위모형(submodel)을 만드는 데에도 사용된다. 이 때문에 반사실은 do-operator와 병렬적인 별도 층이 아니라, **do 연산을 포함해 더 복합적인 비교를 수행하는 상위 질의**로 이해하는 것이 정확하다.

## 1.3.5 3층: 반사실(Counterfactual) — \(P(Y_x \mid X = x',\, Y = y')\)

**직관.** 반사실 층위는 이미 일어난 사실을 전제로, 다르게 행동했더라면 어떻게 되었을지를 묻는다. 2층과의 결정적 차이는 **실제로 관측된 사실이 조건으로 들어간다**는 점이다.

      - 아스피린을 복용한 철수가, 복용하지 않았더라면 두통이 지속되었을까?

      - 대학에 진학하지 않은 사람이 진학했더라면 임금은?

      - 광고를 실제로 집행하지 않은 기업이 집행했더라면 매출은?

이런 질문은 \(\mathrm{do}\)만으로는 부족할 수 있다. 관측된 개인의 역사가 조건에 포함되기 때문이다. 2층이 “무작위로 한 단위를 골라 \(X\)를 바꾼다면?”을 묻는다면, 3층은 “실제로 \(X=x'\)였고 \(Y=y'\)였던 바로 그 단위가, \(x\)였더라면?”을 묻는다.

    **잠재결과와의 연결.** 단위 \(i\)에 대해

    \[
      Y_i(x) \equiv \text{단위 } i \text{에 } X=x \text{로 개입했을 때의 } Y \text{의 값}
    \]



    로 두면, 3층의 질문은 관측 사실을 조건으로 붙인 확률로 쓸 수 있다.

    \[
      P(Y_x = y \mid X = x',\, Y = y').
    \]



    여기서 \(x \neq x'\)이면 진정한 반사실이다.

법·정책에서 자주 쓰이는 양 가운데 하나는 처치를 받은 집단에 대한 반사실적 평균, 예를 들어 \(\mathbb{E}[Y_i(0) \mid T_i = 1]\) — “실제로 처치를 받은 사람들이 받지 않았더라면” — 이다. 이것은 \(\mathrm{do}(T=0)\) 하에서의 주변 분포와 동일한 질문이 **아니다**. 2층은 무작위로 선택된 단위에 개입하는 상황을 묻는 반면, 3층은 특정 처치 상태에 있었던 단위를 조건으로 건다.

SCM에서 반사실 계산은 세 단계로 요약된다. (1) **추론(Abduction)**: 관측 사실에서 배경변수 \(U\)를 추론한다. (2) **행동(Action)**: \(\mathrm{do}\)로 처치를 바꾼다. (3) **예측(Prediction)**: 변경된 모형에서 결과를 계산한다. 이 세 단계는 반사실이 단순한 개입 분포가 아니라, **같은 배경 맥락을 공유한 실제 세계와 가상 세계를 연결하는 연산**임을 보여 준다. 그래서 반사실은 사다리의 꼭대기에 놓인다.

    ## 1.3.6 층위 간 환원 불가능성 — 직관적 논증
    세 층위가 서로 환원 불가능하다는 것은 단순한 구호가 아니라, 동일한 하위 층 정보를 공유하지만 상위 층에서 달라지는 두 개의 SCM을 구성해 보일 수 있다.

    **1층 \(\not\Rightarrow\) 2층.** 같은 \(P(Y \mid X)\)를 주지만 \(P(Y \mid \mathrm{do}(X))\)가 다른 두 모형을 생각하자.

    *모형 A* (교란 \(Z\)): \(Z \to X \to Y\), \(Z \to Y\). 예를 들어

    \[
      Z \sim \mathrm{Bernoulli}(0.5), \quad X = Z + \varepsilon_X, \quad Y = X + Z + \varepsilon_Y.
    \]

:::

    *모형 B* (교란 없음): \(X \to Y\),

    \[
      X \sim \mathrm{Bernoulli}(0.5), \quad Y = X + \varepsilon_Y.
    \]

:::

    적절히 잡음을 잡으면 두 모형에서 \(P(Y \mid X)\)를 같게 맞출 수 있어도, \(\mathrm{do}(X)\)에 따른 \(Y\)의 분포는 다를 수 있다. 즉 **관측 조건부 분포만으로 개입 분포가 결정되지 않는다**.

    **2층 \(\not\Rightarrow\) 3층.** 같은 개입 분포를 주지만 반사실적 종속 구조가 다른 두 잠재결과 모형을 생각할 수 있다.

    *모형 C*: \(Y(1) = U\), \(Y(0) = 1 - U\), \(U \sim \mathrm{Bernoulli}(0.5)\).

    *모형 D*: \(Y(1) = U_1\), \(Y(0) = U_0\), \(U_1, U_0\) i.i.d. \(\mathrm{Bernoulli}(0.5)\).

    두 모형에서 \(P(Y \mid \mathrm{do}(X=1))\)와 \(P(Y \mid \mathrm{do}(X=0))\)의 주요 요약이 같아 보이도록 맞출 수 있어도, 예를 들어 \(P(Y(1)=1 \mid Y(0)=0)\) 같은 반사실적 조건부는 모형 C에서는 1, 모형 D에서는 0.5가 될 수 있다. 즉 **개입 분포만으로 반사실 분포가 결정되지 않는다**.

    \[\begin{aligned}
      \text{1층 정보} &\not\Rightarrow \text{2층 정보} \not\Rightarrow \text{3층 정보},\\
      \text{3층 정보} &\Rightarrow \text{2층 정보} \Rightarrow \text{1층 정보}.
    \end{aligned}\]

:::

    ## 1.3.7 구조 인과 모형(SCM)의 정의

      세 층위를 통합해 형식화하는 언어가 **구조 인과 모형(Structural Causal Model, SCM)**이다. SCM은 잠재결과와 DAG를 같은 틀 안에서 다루는 기반이 된다.

    **정의.** SCM \(\mathcal{M}\)은 네 요소의 튜플로 둔다.

    \[
      \mathcal{M} = \langle \mathbf{U},\, \mathbf{V},\, \mathcal{F},\, P(\mathbf{U}) \rangle.
    \]

:::

      - **외생 변수** \(\mathbf{U}\): 모형 밖에서 결정되는 배경·잡음.

      - **내생 변수** \(\mathbf{V}\): 구조 방정식으로 결정되는 변수(처치·결과·공변량 등).

      - **구조 함수** \(\mathcal{F}\): 각 \(V_i\)를 부모와 잡음의 함수로 두는 \(\{f_i\}\).

      - **외생 분포** \(P(\mathbf{U})\): \(\mathbf{U}\)의 결합분포.

    DAG에서 \(V_i\)의 직접 원인 집합을 \(\mathrm{Pa}(V_i)\)라 하면,

    \[
      V_i = f_i(\mathrm{Pa}(V_i),\, U_i)
    \]

:::

    로 쓸 수 있다.

    **예시.** 처치 \(T\), 결과 \(Y\), 교란 \(Z\)에 대해

    \[\begin{aligned}
      \mathbf{U} &= \{U_T, U_Y, U_Z\}, \quad \mathbf{V} = \{Z, T, Y\},\\
      Z &= f_Z(U_Z) = U_Z,\\
      T &= f_T(Z, U_T) = \alpha Z + U_T,\\
      Y &= f_Y(T, Z, U_Y) = \beta T + \gamma Z + U_Y,
    \end{aligned}\]

:::

    이고 \(U_Z, U_T, U_Y\)가 독립 정규라 하자. 이 SCM은 \(Z\)가 \(T\)와 \(Y\)에 공통으로 영향을 주는 교란 구조를 나타낸다. \(\beta\)가 해석상의 「구조적」인과계수에 해당한다.

    ## 1.3.8 SCM에서 세 층위의 도출
    **1층.** \(P(\mathbf{U})\)와 \(\mathcal{F}\)가 주어지면 \(\mathbf{V}\)의 결합분포가 정해지고, 여기서 \(P(Y \mid X)\) 같은 조건부 분포가 나온다.

    **2층 — \(\mathrm{do}\)와 절단.** \(\mathrm{do}(T=t)\)는 \(f_T\)를 상수 \(t\)로 바꾸는 조작으로 이해할 수 있다. \(T\)로 들어오는 화살표가 끊어진 변형 모형 \(\mathcal{M}_{\mathrm{do}(T=t)}\)에서의 분포가 \(P(\mathbf{V} \mid \mathrm{do}(T=t))\)에 대응한다.

    위 선형 예에서 \(\mathrm{do}(T=t)\)이면

    \[\begin{aligned}
      Z &= U_Z, \quad T = t, \quad Y = \beta t + \gamma Z + U_Y,
    \end{aligned}\]


    이므로

    \[
      \mathbb{E}[Y \mid \mathrm{do}(T=t)] = \beta t + \gamma \,\mathbb{E}[Z].
    \]

:::

    예를 들어 위 예시에서 \(Z=U_Z \sim \mathcal{N}(0,1)\)이면 \(\mathbb{E}[Z]=0\)이어서 \(\mathbb{E}[Y \mid \mathrm{do}(T=t)] = \beta t\)이다. 반면 관측 조건부는

    \[
      \mathbb{E}[Y \mid T=t] = \beta t + \gamma \,\mathbb{E}[Z \mid T=t] = \beta t + \gamma \alpha t
    \]

:::

    와 같아, 회귀로 얻는 계수가 \(\beta\)가 아니라 \(\beta + \gamma\alpha\)에 가닿을 수 있다. 이를 한 줄로 쓰면

    \[
      \underbrace{\mathbb{E}[Y \mid T=t]}_{\text{관측}}
      = \underbrace{\mathbb{E}[Y \mid \mathrm{do}(T=t)]}_{\text{인과}} + \underbrace{\gamma \alpha t}_{\text{교란 편향}}
    \]

:::

    와 같이 정리할 수 있다(선형·단순화된 전제 하에서의 표현).

    **3층 — 쌍 세계(twin world).** 반사실 \(Y_i(t)\)는 같은 외생 변수 \(\mathbf{U}_i\)를 공유하되 처치만 \(t\)로 바꾼 구조적 출력으로 정의할 수 있다. 선형 예에서 단위 \(i\)가 \(T_i=1\)이고 \(Y_i=y_i\)를 관측했다면, \(Y_i(1)=\beta + \gamma Z_i + U_{Y,i}=y_i\)로부터 \(Y_i(0)=\gamma Z_i + U_{Y,i}=y_i-\beta\)로 읽는 식의 계산이 가능해진다(모형이 선형이고 잡음이 분해된 특수한 경우). 일반적으로는 \(\tau_i\)가 단위마다 달라 **처치 이질성**이 생긴다.

    ## 1.3.9 세 층위와 SCM의 관계 — 통합적 그림
    한 SCM \(\mathcal{M}\)이 주어지면, 관측 분포(1층), 절단 모형의 분포(2층), 배경 \(\mathbf{U}\)를 고정한 반사실(3층)을 같은 뼈대에서 도출할 수 있다. 핵심은 SCM이 단순한 연관이 아니라 **DGP의 인과 구조**를 명시한다는 점이다. 그만큼 관측 데이터만으로 SCM 전체를 유일하게 학습하는 것은 일반적으로 불가능하고, **영역 지식**이 구조 선택에 들어간다.

    \[
      \mathcal{M} = \langle \mathbf{U}, \mathbf{V}, \mathcal{F}, P(\mathbf{U}) \rangle
      \;\Rightarrow\;
      \begin{cases}
        \text{1층: } & P(\mathbf{V}) \text{에서 조건부 분포} \\
        \text{2층: } & P^{\mathcal{M}_{\mathrm{do}(X=x)}}(\mathbf{V}) \\
        \text{3층: } & \mathbf{U} \text{ 고정 하 반사실 } Y_x
      \end{cases}
    \]

:::

    ## 1.3.10 \(\mathrm{do}\) 연산자의 규칙 — do-calculus

      Pearl은 \(\mathrm{do}\)를 포함한 표현을 관측 분포로 바꾸는 규칙 체계 **do-calculus**를 제시했다. DAG \(G\) 위에서 \(G_{\overline{X}}\)는 \(X\)로 들어오는 화살표를 제거한 그래프, \(G_{\underline{X}}\)는 \(X\)에서 나가는 화살표를 제거한 그래프로 둔다(표기는 문헌마다 동일하지 않을 수 있으니 3·4장에서 다시 맞춘다).

    **규칙 1 (관측의 삽입·삭제).** \((Y \perp\!\!\!\perp Z \mid X, W)_{G_{\overline{X}}}\)이면

    \[
      P(Y \mid \mathrm{do}(X), Z, W) = P(Y \mid \mathrm{do}(X), W).
    \]

:::

    **규칙 2 (행동과 관측의 교환).** \((Y \perp\!\!\!\perp Z \mid X, W)_{G_{\overline{X}\underline{Z}}}\)이면

    \[
      P(Y \mid \mathrm{do}(X), \mathrm{do}(Z), W) = P(Y \mid \mathrm{do}(X), Z, W).
    \]

:::

    **규칙 3 (행동의 삽입·삭제).** 일부 그래프 조건 하에

    \[
      P(Y \mid \mathrm{do}(X), \mathrm{do}(Z), W) = P(Y \mid \mathrm{do}(X), W)
    \]

:::

    와 같은 변형이 허용된다(정확한 그래프 조건은 \(Z(W)\) 등 세부 표기와 함께 원문을 따른다).

    Huang and Valtorta(2006), Shpitser and Pearl(2006) 등에 이어, do-calculus의 **완전성(completeness)**이 논의된다. 즉, 식별 가능한 인과량은 이 규칙들의 반복 적용으로 표현될 수 있다는 취지의 결과로 이해할 수 있다.

    ## 1.3.11 조정 공식 — do-calculus의 첫 응용
    백도어 기준을 만족하는 공변량 집합 \(\mathbf{Z}\)가 있을 때,

    \[
      P(Y = y \mid \mathrm{do}(X = x)) = \sum_{\mathbf{z}} P(Y = y \mid X = x,\, \mathbf{Z} = \mathbf{z})\, P(\mathbf{Z} = \mathbf{z})
    \]

:::

    와 같이 \(\mathrm{do}\)가 없는 표현으로 바뀐다(이산 경우). 연속형이면 합 대신 적분이 된다.

    \[
      P(Y = y \mid \mathrm{do}(X = x)) = \int P(Y = y \mid X = x,\, \mathbf{Z} = \mathbf{z})\, p(\mathbf{z})\, d\mathbf{z}.
    \]

:::

    이것이 역학에서 말하는 표준화·주변화와 대응한다. 중요한 것은 \(\mathrm{do}\) 식이 **관측 가능한 확률만**으로 쓰일 때, 그 인과량이 데이터로부터 **식별**된다는 점이다. 4장에서 백도어 기준과 함께 다시 본다.

    ## 1.3.12 세 층위와 이 책의 구성

      **제2부**(실험)와 **제4부**(식별 전략)는 주로 **2층** 질문 — ATE, ATT, LATE 등 \(\mathrm{do}(T)\)에 대한 요약 — 을 다룬다. 개입 실험·준실험, 또는 충분한 구조 가정으로 \(\mathrm{do}\) 표현을 관측 분포로 바꾸는 것이 핵심이다.

      **제5부**(매개 등)는 **2층과 3층의 경계**에 놓인다. 자연 직접·간접효과 같은 대상은 반사실을 요구하고, 단순한 \(\mathrm{do}\) 한 방으로 정리되지 않을 수 있다.

      **제6부**(반모수 이론)는 **1·2층의 추정·효율**을 중심으로 하되, 부분 식별·민감도에서는 3층의 반사실 구조가 다시 등장한다.

    ## 1.3.13 인과 사다리와 현대 AI의 한계

      현대 ML과 대규모 언어모델은 \(P(Y \mid X)\)를 매우 정밀하게 근사할 수 있지만, 그것만으로 \(P(Y \mid \mathrm{do}(X))\)나 \(P(Y_x \mid X=x', Y=y')\)에 자동으로 도달하지는 않는다. 이는 데이터 양의 문제가 아니라 질문 층위의 문제다.

      따라서 인과 추론 맥락에서 ML은 필요하지만 충분하지 않은 도구다. 2층·3층 질문에는 구조 가정과 식별 논리가 추가되어야 한다.

    ## 1.3.14 철학적 함의와 실무적 메시지

      반사실 층위는 도덕적 책임, 법적 인과, 정책 귀속의 핵심 언어와 직접 연결된다. "그 행위가 없었더라면 결과가 달랐는가"라는 but-for 질문은 3층 반사실 문법의 전형이다.

      실무적으로는 질문의 층위를 먼저 명확히 하고, 그 층위에 맞는 수학적 언어와 가정을 선택해야 한다. 이 순서를 거꾸로 두면 정교한 계산이 오히려 해석 오류를 강화할 수 있다.

<svg width="400" height="120" viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg">
        <text x="200" y="20" text-anchor="middle" font-size="11" fill="#1e4d6b" font-weight="700">관측으로 직접 얻는 것 vs. 가정이 필요한 것</text>
        <rect x="30" y="40" width="100" height="60" rx="6" fill="#f0f4f8" stroke="#1e4d6b"/>
        <text x="80" y="68" text-anchor="middle" font-size="10" font-weight="600">연관</text>
        <text x="80" y="86" text-anchor="middle" font-size="8.5" fill="#555">회귀·상관</text>
        <line x1="130" y1="70" x2="170" y2="70" stroke="#333" stroke-width="1.5" marker-end="url(#arr13)"/>
        <defs>
          <marker id="arr13" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#333"/></marker>
        </defs>
        <text x="150" y="62" text-anchor="middle" font-size="8" fill="#888">가정</text>
        <rect x="170" y="40" width="100" height="60" rx="6" fill="#e8f5ef" stroke="#1d6b4a"/>
        <text x="220" y="68" text-anchor="middle" font-size="10" font-weight="600">개입</text>
        <text x="220" y="86" text-anchor="middle" font-size="8.5" fill="#555">do-분포</text>
        <line x1="270" y1="70" x2="310" y2="70" stroke="#333" stroke-width="1.5" marker-end="url(#arr13)"/>
        <rect x="310" y="40" width="60" height="60" rx="6" fill="#f5eef8" stroke="#6b4c9a"/>
        <text x="340" y="75" text-anchor="middle" font-size="13" font-weight="700">?</text>
        <text x="200" y="112" text-anchor="middle" font-size="9" fill="#666">반사실은 개입·구조 위에 더 얹은 정보가 필요할 때가 많다</text>
      </svg>

      **그림 2.** 연관에서 출발해, 인과 가정으로 개입 분포를 정의하고, 반사실은 그 위의 한 단계.

:::


:::
summary

      핵심 요약

        - Pearl의 인과 사다리는 연관 \(P(Y \mid X)\) → 개입 \(P(Y \mid \mathrm{do}(X))\) → 반사실 \(P(Y_x \mid X=x',\, Y=y')\)의 세 층위로 정리되며, 상위에서 하위로의 환원은 일반적으로 불가능하다.

        - 세 층위는 See(연관) · Do(개입) · Imagine(반사실)의 동사 위계로도 이해할 수 있고, 질문 층위가 필요한 가정을 결정한다.

        - SCM \(\mathcal{M} = \langle \mathbf{U}, \mathbf{V}, \mathcal{F}, P(\mathbf{U}) \rangle\)은 세 층위를 단일 수학적 대상에서 연결하는 틀이다.

        - \(\mathrm{do}(X=x)\)는 구조 함수를 상수로 바꾸는 절단 조작으로 해석할 수 있으며, \(P(Y \mid X)\)와 \(P(Y \mid \mathrm{do}(X))\)의 차이가 교란 편향으로 연결된다.

        - 반사실 계산은 추론(Abduction)→행동(Action)→예측(Prediction)의 3단계로 정리되며, 2층 정보만으로는 일반적으로 3층을 복원할 수 없다.

        - do-calculus는 \(\mathrm{do}\)를 관측 분포로 바꾸는 규칙 체계이고, 조정 공식은 대표적인 응용이다. 식별이란 \(\mathrm{do}\) 표현이 관측 가능한 확률로 쓰일 수 있는가의 문제다.

:::

      다음 절([1.4 성별은 원인이 될 수 없는가 — 비판적 검토](ch01-04-gender-causality-debate.html))에서
      Holland의 조작가능성 원칙을 둘러싼 현대 논쟁을 정리한 뒤, [2장 개요](ch02-00-potential-outcomes-framework-overview.html)와
      [2.1 단위·처치·잠재결과](ch02-01-unit-treatment-potential-outcomes.html)로 넘어가 잠재결과 프레임워크를 형식화한다.
