---
title: 18.1 CATE의 정의와 식별
description: CATE는 특정 공변량 값을 가진 집단에서의 평균 처치효과를 뜻한다. 이 절은 CATE의 정의, ATE·ATT와의 관계, 식별 가정, 추정 방법, 정책평가에서의 의미를 수식과 시각화와 함께 정리한다.
---

# 18.1 CATE의 정의와 식별

평균 처치효과 \(ATE\)는 정책의 전반적 방향을 보여주지만, 실제 정책은 거의 항상 사람마다 다르게 작동한다. 어떤 집단에는 매우 효과적이고, 다른 집단에는 거의 무효이거나 부정적일 수 있다. CATE는 바로 이런 **이질적 처치효과(heterogeneous treatment effects)**를 다루는 핵심 개념이다.

앞 절에서 본 것처럼 평균효과만으로는 정책의 분포적 작동방식을 이해하기 어렵다. 그래서 18장의 출발점은 “이질적 효과를 어떻게 정의할 것인가”이다. 정의가 흔들리면 이후의 subgroup 분석도, 정책 타겟팅도 모두 불안정해진다.

## CATE의 정의

CATE는 특정 공변량 벡터 \(X=x\)를 가진 단위에서의 평균 처치효과다.

\[
\tau(x)=\mathbb{E}[Y(1)-Y(0)\mid X=x].
\]

이 정의는 아주 중요하다. CATE는 개별 단위의 효과 \(Y_i(1)-Y_i(0)\)를 관찰한다는 뜻이 아니다. 개별 효과는 여전히 직접 볼 수 없고, 그 대신 **같은 특성 \(x\)를 가진 집단 안에서의 평균 효과**를 본다는 뜻이다.

## ATE, ATT, CATE의 관계

이 세 개념은 경쟁하는 개념이 아니라 서로 연결된 개념이다.

\[
ATE=\mathbb{E}[\tau(X)].
\]

\[
ATT=\mathbb{E}[\tau(X)\mid D=1].
\]

즉 ATE는 CATE를 전체 분포에 대해 평균낸 것이고, ATT는 처치받은 집단의 \(X\) 분포에 대해 평균낸 것이다. 따라서 CATE를 이해하면 ATE와 ATT가 어떤 평균의 결과인지 더 분명하게 보인다.

## 시각적으로 보면 무엇을 뜻하는가

아래 그림은 같은 정책이라도 공변량 \(X\) 값에 따라 효과가 달라질 수 있음을 단순화해서 보여준다.

<figure class="chapter-figure">
  <svg viewBox="0 0 760 380" role="img" aria-labelledby="cate-visual-title cate-visual-desc">
    <title id="cate-visual-title">조건부 평균처치효과 CATE 시각화</title>
    <desc id="cate-visual-desc">가로축은 공변량 X, 세로축은 기대 결과를 나타내며 처치와 비처치 결과곡선 사이의 간격이 X에 따라 달라지는 모습을 보여준다.</desc>
    <rect x="0" y="0" width="760" height="380" fill="#fbfaf4"></rect>
    <line x1="90" y1="315" x2="700" y2="315" stroke="#293241" stroke-width="2"></line>
    <line x1="90" y1="315" x2="90" y2="55" stroke="#293241" stroke-width="2"></line>
    <text x="705" y="321" font-size="16" fill="#293241">공변량 X</text>
    <text x="28" y="65" font-size="16" fill="#293241">기대 결과</text>

    <path d="M120 270 C220 250, 300 220, 400 195 S560 145, 670 125" fill="none" stroke="#4f6d7a" stroke-width="4"></path>
    <path d="M120 285 C220 275, 300 255, 400 240 S560 215, 670 205" fill="none" stroke="#d06b36" stroke-width="4"></path>

    <text x="575" y="128" font-size="15" fill="#4f6d7a">E[Y(1)|X=x]</text>
    <text x="575" y="208" font-size="15" fill="#d06b36">E[Y(0)|X=x]</text>

    <line x1="220" y1="258" x2="220" y2="272" stroke="#2f5d50" stroke-width="4"></line>
    <line x1="420" y1="201" x2="420" y2="236" stroke="#2f5d50" stroke-width="4"></line>
    <line x1="610" y1="144" x2="610" y2="212" stroke="#2f5d50" stroke-width="4"></line>

    <text x="142" y="245" font-size="14" fill="#2f5d50">작은 CATE</text>
    <text x="438" y="188" font-size="14" fill="#2f5d50">중간 CATE</text>
    <text x="620" y="176" font-size="14" fill="#2f5d50">큰 CATE</text>

    <rect x="110" y="24" width="315" height="40" rx="8" fill="#eef4ea" stroke="#b7c8b2"></rect>
    <text x="126" y="49" font-size="15" fill="#2f5d50">두 곡선 사이의 세로 간격이 바로 \(\tau(x)\): X에 따라 효과가 달라질 수 있다</text>
  </svg>
  <figcaption>공변량 \(X\) 값에 따라 처치효과 \(\tau(x)\)가 달라질 수 있다는 점을 보여주는 도식.</figcaption>
</figure>

이 그림의 요점은 간단하다. 평균효과 하나만 보면 두 곡선 사이의 평균 간격만 보게 되지만, CATE는 **어느 구간에서 효과가 크고 작은지**를 본다.

## 식별은 어떻게 가능한가

무작위 실험이라면 \(D \perp (Y(1),Y(0))\mid X\)가 비교적 설득력 있게 성립하므로, 각 \(X=x\) 집단 안에서 처치군과 통제군을 비교해 CATE를 식별할 수 있다.

관찰자료에서는 보통 다음 두 가정이 필요하다.

\[
(Y(1),Y(0)) \perp D \mid X
\]

\[
0 < e(X)=P(D=1\mid X) < 1
\]

첫 번째는 **조건부 독립성(conditional independence)** 또는 selection on observables 가정이고, 두 번째는 **중첩성(overlap, positivity)** 가정이다.

이 두 가정이 성립하면

\[
\tau(x)
=
\mathbb{E}[Y\mid D=1,X=x]
-
\mathbb{E}[Y\mid D=0,X=x]
\]

으로 쓸 수 있다.

## 왜 CATE 식별이 평균효과보다 더 어려운가

ATE는 전체 표본을 평균내므로 어느 정도 정보가 축적된다. 반면 CATE는 \(X=x\) 근방의 더 좁은 집단 안에서 비교해야 하므로 표본이 훨씬 희박해진다. 이 때문에 다음 문제가 생긴다.

- 차원이 높은 \(X\)에서는 근처 관측치가 드물다.
- overlap이 약한 영역에서는 처치군 또는 비교군이 거의 없다.
- 작은 하위집단에서는 분산이 매우 커진다.
- 모형의 함수형 가정에 민감해질 수 있다.

즉 CATE는 평균효과보다 더 풍부한 정보를 주지만, 동시에 더 어려운 추정 문제다.

## 추정 전략

가장 단순한 접근은 회귀모형에서 상호작용항을 넣는 것이다.

\[
\mathbb{E}[Y\mid D,X]
=
\alpha + X'\beta + D\gamma + D\cdot X'\delta.
\]

이 경우

\[
\tau(x)=\gamma + x'\delta
\]

처럼 해석할 수 있다. 하지만 실제 이질성이 비선형적이고 복잡하면 이런 선형 상호작용만으로는 부족할 수 있다.

그래서 최근에는 다음 같은 방법이 널리 사용된다.

- **S-learner / T-learner / X-learner**: 머신러닝 기반 outcome modeling
- **DR-learner**: outcome model과 propensity model을 함께 써서 강건성 강화
- **causal forest**: 비선형적 이질성을 유연하게 추정
- **DML / R-learner**: 고차원 \(X\)와 nuisance estimation을 분리해 추정

## 정책평가 사례

직업훈련 정책을 생각해보자. 평균적으로는 취업률을 2%p 높였다고 해도, 장기실업자에게는 8%p, 이미 노동시장 연결이 강한 사람에게는 0%p일 수 있다. 장학금 정책도 평균 효과는 작아 보여도 저소득·학업취약 학생에게는 매우 클 수 있다. 이런 경우 CATE는 정책을 “폐기할지”가 아니라 “어떻게 더 잘 설계할지”를 알려준다.

## 해석상의 주의

- CATE는 탐색적 패턴과 인과적 식별을 구분해야 한다.
- 특정 \(x\)에서 추정치가 크다고 해서 반드시 신뢰도도 높은 것은 아니다.
- 결과를 너무 잘게 쪼개면 다중검정과 재현성 문제가 커진다.
- 정책 타겟팅에 쓰려면 효과뿐 아니라 비용, 형평성, 실행가능성까지 함께 봐야 한다.

## 정리

CATE는 평균효과 뒤에 숨겨진 정책의 실제 분포를 드러내는 핵심 개념이다. 그러나 그만큼 식별과 추정이 더 어렵고, 더 엄격한 해석 규율이 필요하다. 특히 실제 연구에서는 CATE를 가장 손쉽게 구현한다는 이유로 서브그룹 분석으로 곧바로 넘어가곤 하는데, 바로 그 지점에서 많은 오해가 발생한다. 다음 절에서는 이질적 효과 분석이 왜 쉽게 잘못된 subgroup 이야기로 흘러가는지를 짚는다.
