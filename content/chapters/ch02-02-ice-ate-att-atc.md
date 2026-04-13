---
title: 2.2 개인 인과효과와 평균 인과효과 - ICE · ATE · ATT · ATC
description: 잠재결과를 정의한 뒤에는 효과를 어떤 수준에서 요약할지 정해야 한다. 이 절은 개인 인과효과와 평균 인과효과의 관계를 정리하고, 왜 질문에 따라 목표 모수가 달라지는지를 설명한다.
---

# 2.2 개인 인과효과와 평균 인과효과 - ICE · ATE · ATT · ATC

2.1절에서 단위, 처치, 잠재결과를 정의했다면 다음 질문은 자연스럽게 "그래서 효과를 무엇으로 정의할 것인가"로 이어진다. 이 질문은 단순해 보이지만 실제로는 연구의 목표 모수를 결정하는 핵심 단계다. 같은 자료를 사용하더라도 개인 수준 효과를 묻는지, 전체 모집단 평균효과를 묻는지, 실제 처치집단에 대한 효과를 묻는지에 따라 해석과 추정 전략이 달라진다.

정책평가에서는 특히 이 구분이 중요하다. 보편 정책 확대 여부를 판단할 때는 전체 평균효과가 중요하고, 이미 프로그램에 참여한 사람들에게 효과가 있었는지를 따질 때는 처치군 평균효과가 중요하다. 아래에서는 개인 인과효과, 평균 인과효과, 그리고 그 하위 개념들을 차례로 정리한다.

## 2.2.1 왜 효과를 구분해서 정의해야 하는가

잠재결과 \(Y_i(1)\), \(Y_i(0)\)을 정의한 뒤의 질문은 곧바로 "효과를 어떻게 정의할 것인가"로 옮겨 간다. 여기서 효과는 하나의 값이 아니라 여러 수학적 대상으로 갈라진다. 대표적으로 ICE, ATE, ATT, ATC, CATE, LATE가 있다. 누구를 기준으로 평균을 내는지, 어떤 하위집단을 대상으로 삼는지에 따라 의미가 달라지기 때문이다.

정책 질문과 임상 질문은 비슷해 보여도 목표 모수가 다르다. 예를 들어 전국 정책을 확대할지 말지를 판단할 때는 전체 평균효과인 ATE가 중요하다. 반면 이미 참여한 사람들에게 실제로 효과가 있었는가를 묻는다면 ATT가 더 자연스럽다. 개인에게 처치를 권고할지 판단하는 문제는 다시 CATE나 개인 반사실과 가까워진다.

## 2.2.2 개인 인과효과(ICE)

개인 인과효과(individual causal effect)는 각 단위가 처치를 받았을 때와 받지 않았을 때 결과 차이로 정의된다.

\[
\tau_i \equiv Y_i(1) - Y_i(0)
\]

이는 동일 단위 \(i\)의 두 잠재결과 차이이며, 둘 중 하나는 반드시 반사실이다. 따라서 ICE는 원칙적으로 직접 관측되지 않는다. 이것이 인과추론이 본질적으로 어려운 이유다.

일반적으로 \(\tau_i \neq \tau_j\)이며, 이것이 처치효과 이질성이다. 이질성은 관측 가능한 공변량 \(\mathbf{X}_i\)에 따라 나타날 수도 있고, 관측되지 않는 요인 \(U_i\) 때문에 생길 수도 있다.

실제로는 관측결과가 다음과 같이 주어진다.

\[
Y_i^{\mathrm{obs}} =
\begin{cases}
Y_i(1) & \text{if } D_i = 1, \\
Y_i(0) & \text{if } D_i = 0.
\end{cases}
\]

즉 한 단위에 대해 두 잠재결과를 동시에 볼 수 없기 때문에 \(\tau_i\)를 직접 계산할 수 없다.

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

특수한 구조 가정, 예를 들어 모든 개인에게 효과가 동일하다는 강한 동질성 가정이 있으면 개인 효과를 평균 효과와 거의 같은 것으로 다룰 수 있다. 그러나 보통 정책평가에서는 이런 가정을 쉽게 둘 수 없으므로 평균효과를 명시적으로 정의해야 한다.

## 2.2.3 평균 인과효과(ATE)

전체 모집단의 평균 인과효과는 다음과 같이 정의된다.

\[
\mathrm{ATE} \equiv \mathbb{E}[\tau_i]
= \mathbb{E}[Y_i(1)-Y_i(0)]
= \mathbb{E}[Y_i(1)]-\mathbb{E}[Y_i(0)].
\]

ATE는 전체 모집단에 대해 처치를 시행했을 때의 평균 효과다. 보편 정책의 평균 성과를 묻는 질문에 자연스럽다.

무작위배정이 성립해 \(\{Y_i(1),Y_i(0)\}\perp\!\!\!\perp D_i\)라면 ATE는 관측집단 평균차이로 식별된다.

\[
\mathrm{ATE}
= \mathbb{E}[Y_i^{\mathrm{obs}} \mid D_i=1]
- \mathbb{E}[Y_i^{\mathrm{obs}} \mid D_i=0].
\]

즉 처치군과 통제군의 평균차이는 무작위실험에서 ATE의 비편향 추정량이 된다.

## 2.2.4 처치군 평균 인과효과(ATT)

처치군 평균 인과효과는 실제로 처치를 받은 사람들을 기준으로 정의된다.

\[
\mathrm{ATT}
\equiv \mathbb{E}[\tau_i \mid D_i=1]
= \mathbb{E}[Y_i(1)\mid D_i=1] - \mathbb{E}[Y_i(0)\mid D_i=1].
\]

ATT는 프로그램 유지, 현재 수혜자 성과 평가, 기존 참여자 분석처럼 "실제로 처치를 받은 사람들에게 효과가 있었는가"를 묻는 상황에 잘 맞는다.

관측평균차이는 다음과 같이 ATT와 선택편향으로 분해된다.

\[
\underbrace{\mathbb{E}[Y_i^{\mathrm{obs}}\mid D_i=1]-\mathbb{E}[Y_i^{\mathrm{obs}}\mid D_i=0]}_{\text{관측 평균 차이}}
=
\underbrace{\mathrm{ATT}}_{\text{처치군 효과}}
+
\underbrace{\mathbb{E}[Y_i(0)\mid D_i=1]-\mathbb{E}[Y_i(0)\mid D_i=0]}_{\text{선택 편향}}.
\]

관측연구가 어려운 핵심은 마지막 선택편향 항을 직접 볼 수 없다는 점이다. 처치받은 사람과 받지 않은 사람이 원래부터 다를 수 있기 때문이다.

## 2.2.5 통제군 평균 인과효과(ATC)

통제군 평균 인과효과는 현재 처치를 받지 않은 사람들에게 처치를 확대했을 때의 평균 효과다.

\[
\mathrm{ATC}
\equiv \mathbb{E}[\tau_i \mid D_i=0]
= \mathbb{E}[Y_i(1)\mid D_i=0] - \mathbb{E}[Y_i(0)\mid D_i=0].
\]

ATC는 정책 확장(scale-up) 문제에서 특히 중요하다. 현재 비참여자에게 프로그램을 확대하면 어떤 평균 효과가 나올지를 묻기 때문이다.

## 2.2.6 세 추정량의 관계

처치 비율을 \(\pi \equiv P(D_i=1)\)라고 하면 세 추정량은 다음 관계로 연결된다.

\[
\mathrm{ATE} = \pi\cdot \mathrm{ATT} + (1-\pi)\cdot \mathrm{ATC}.
\]

또한 무작위배정처럼 \(\{Y_i(1),Y_i(0)\}\perp\!\!\!\perp D_i\)가 성립하면 \(\mathrm{ATE}=\mathrm{ATT}=\mathrm{ATC}\)가 된다. 그러나 선택이 있는 관측자료에서는 보통 이 셋이 다르다.

아래 완전 잠재결과 예시에서는 ATT가 가장 크고 ATC가 가장 작다.

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

이때 관측 평균차이는 다음처럼 ATT와 선택편향의 합으로 읽힌다.

\[
\mathbb{E}[Y^{\mathrm{obs}}\mid D=1]-\mathbb{E}[Y^{\mathrm{obs}}\mid D=0]
= \frac{10}{3}\approx 3.33
= \underbrace{3.67}_{\mathrm{ATT}} + \underbrace{(-0.33)}_{\text{선택 편향}}.
\]

## 2.2.7 CATE(조건부 평균 처치효과)

조건부 평균 처치효과는 공변량 값에 따라 평균효과가 어떻게 달라지는지를 나타낸다.

\[
\tau(\mathbf{x}) \equiv \mathbb{E}[\tau_i \mid \mathbf{X}_i=\mathbf{x}]
= \mathbb{E}[Y_i(1)-Y_i(0)\mid \mathbf{X}_i=\mathbf{x}].
\]

CATE는 효과 이질성 구조를 \(\mathbf{X}\)의 함수로 표현한다. ATE, ATT, ATC는 CATE를 서로 다른 분포로 주변화한 값으로 해석할 수 있다.

\[
\mathrm{ATE}=\int \tau(\mathbf{x})\,dP(\mathbf{x}),\quad
\mathrm{ATT}=\int \tau(\mathbf{x})\,dP(\mathbf{x}\mid D=1),\quad
\mathrm{ATC}=\int \tau(\mathbf{x})\,dP(\mathbf{x}\mid D=0).
\]

개인화된 정책 타기팅은 종종 \(d^*(\mathbf{x})=\mathbb{1}[\tau(\mathbf{x})>0]\) 같은 규칙으로 표현된다.

## 2.2.8 효과 척도: 차이 vs 비율

같은 잠재결과라도 어떤 척도로 효과를 읽는지에 따라 해석이 달라진다. 이진 결과에서는 보통 위험차(RD), 위험비(RR), 오즈비(OR)를 구분한다.

\[
\mathrm{RD}=P(Y_i(1)=1)-P(Y_i(0)=1),\quad
\mathrm{RR}=\frac{P(Y_i(1)=1)}{P(Y_i(0)=1)}.
\]

\[
\mathrm{OR}=
\frac{P(Y_i(1)=1)/P(Y_i(1)=0)}{P(Y_i(0)=1)/P(Y_i(0)=0)}.
\]

효과 수정(effect modification)은 척도 의존적일 수 있으므로, 결과 보고 시 어떤 척도를 사용했는지 분명히 적어야 한다.

## 2.2.9 LATE(국소 평균 처치효과)

도구변수 맥락에서는 순응자(compliers) 부분 모집단의 평균효과인 LATE(Imbens & Angrist, 1994)를 사용한다.

\[
\mathrm{LATE} \equiv \mathbb{E}[\tau_i \mid \text{complier}].
\]

LATE는 ATE, ATT, ATC와 다른 목표 모수이며, 외부 타당도 해석을 별도로 요구한다.

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

즉 연구 질문이 무엇인지, 보편 정책인지, 현재 참여자 평가인지, 정책 확대인지, 개인화 의사결정인지를 먼저 정해야 목표 모수와 추정 전략이 정해진다.

## 2.2 핵심 요약

- ICE \(\tau_i=Y_i(1)-Y_i(0)\)는 개인 수준 효과지만 직접 관측할 수 없다.
- ATE는 전체 평균, ATT는 처치군 평균, ATC는 통제군 평균 효과를 뜻한다.
- 세 추정량은 \(\mathrm{ATE}=\pi\mathrm{ATT}+(1-\pi)\mathrm{ATC}\) 관계로 연결된다.
- 관측 평균차이는 ATT와 선택편향의 합으로 분해된다.
- CATE는 이질성 구조를 보여 주며, ATE, ATT, ATC는 CATE의 주변화로 볼 수 있다.
