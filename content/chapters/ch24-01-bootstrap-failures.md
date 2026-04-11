---
title: 22장. 부트스트랩과 실패 사례
description: 부트스트랩이 언제 유용하고 언제 실패하는지, 정책평가 연구에서 왜 이를 조심해야 하는지 소개한다.
---

# 22장. 부트스트랩과 실패 사례

정책평가 연구에서 표준오차와 신뢰구간을 계산할 때 부트스트랩은 매우 매력적인 도구다. 모형이 복잡하거나 추정량이 닫힌 형태의 분산식을 갖지 않을 때도, 표본을 반복 재표집하여 분포를 근사할 수 있기 때문이다. 특히 매칭, 머신러닝 기반 추정, 다단계 추정, 행정자료 결합처럼 분석 절차가 길어질수록 부트스트랩은 자연스러운 선택처럼 보인다.

하지만 부트스트랩은 “아무 추정량에나 자동으로 붙일 수 있는 만능 분산추정 장치”가 아니다. 어떤 추정량은 부트스트랩이 잘 근사하지만, 어떤 추정량은 경계(boundary), 비정칙성(non-regularity), 표본선택, 모형선택 단계 때문에 표준 부트스트랩이 실패한다. 이 장은 바로 그 경계를 설명하기 위한 장이다.

## 22.0.1 부트스트랩의 기본 직관

원표본 \(P_n\)에서 추정량 \(\hat\theta=T(P_n)\)를 계산했다고 하자. 부트스트랩은 원표본에서 복원추출로 새로운 표본 \(P_n^*\)를 여러 번 만들고,

\[
\hat\theta^{*(b)} = T(P_n^{*(b)}), \qquad b=1,\dots,B
\]

를 계산해 \(\hat\theta\)의 표집분포를 근사한다. 이렇게 얻은 \(\{\hat\theta^{*(b)}\}\)의 분산, 분위수, 편향을 이용해 표준오차와 신뢰구간을 만든다.

정책평가 실무에서 이 직관은 매우 강력하다. 예를 들어

- matching estimator
- inverse probability weighted estimator
- doubly robust estimator
- synthetic control
- causal forest 기반 policy value

같이 닫힌 분산식이 복잡한 추정량들에서 부트스트랩은 계산적으로 편리하다.

## 22.0.2 왜 실패할 수 있는가

부트스트랩이 잘 작동하려면 원표본에서의 확률근사와 재표집 표본에서의 확률근사가 서로 충분히 비슷해야 한다. 하지만 추정량이 비정칙적이면

\[
\sqrt{n}(\hat\theta^*-\hat\theta)
\]

의 분포가

\[
\sqrt{n}(\hat\theta-\theta_0)
\]

를 잘 따라가지 못할 수 있다. 직관적으로는 원표본이 아주 작은 구조 변화에도 불연속적으로 반응하는 경우다.

대표적으로 다음이 문제를 일으킨다.

- 최대값, 최소값, threshold 같은 경계형 함수
- 모형선택 이후 추정(post-selection inference)
- 최적 bandwidth를 함께 고르는 절차
- 매칭처럼 이웃 선택이 이산적으로 바뀌는 추정기
- 부분식별처럼 점이 아니라 구간을 다루는 문제

## 22.0.3 정책평가에서 왜 중요한가

정책평가 연구자는 단지 “효과가 있는가”만 묻지 않는다. 효과의 불확실성이 얼마나 큰지, 정책권고가 얼마나 안정적인지, 다른 표본에서 재현될 가능성이 있는지까지 묻는다. 부트스트랩을 잘못 쓰면 점추정치보다 오히려 더 위험한 오판을 할 수 있다. 예를 들어 정책효과가 통계적으로 유의하다고 결론 내렸는데, 사실은 신뢰구간 계산이 잘못되어 있었던 것일 수 있다.

행정자료 기반 정책평가에서는 표본이 커 보여도 구조가 복잡한 경우가 많다. 군집, 불균형 패널, 정책도입 시점의 endogeneity, 튜닝 파라미터 선택, trimming 규칙이 함께 들어가면 “그냥 bootstrap 500회”로 끝내기 어렵다.

## 22.0.4 간단한 시각적 직관

<figure class="figure">
  <svg viewBox="0 0 860 240" role="img" aria-label="부트스트랩의 기본 아이디어">
    <rect x="40" y="45" width="180" height="60" rx="12" fill="#dbeafe" stroke="#2563eb"/>
    <text x="130" y="80" text-anchor="middle" font-size="20" fill="#1d4ed8">원표본</text>
    <rect x="300" y="35" width="160" height="44" rx="10" fill="#ecfeff" stroke="#0891b2"/>
    <rect x="300" y="95" width="160" height="44" rx="10" fill="#ecfeff" stroke="#0891b2"/>
    <rect x="300" y="155" width="160" height="44" rx="10" fill="#ecfeff" stroke="#0891b2"/>
    <text x="380" y="63" text-anchor="middle" font-size="17" fill="#0f766e">재표집 1</text>
    <text x="380" y="123" text-anchor="middle" font-size="17" fill="#0f766e">재표집 2</text>
    <text x="380" y="183" text-anchor="middle" font-size="17" fill="#0f766e">재표집 B</text>
    <rect x="610" y="72" width="190" height="72" rx="12" fill="#fef3c7" stroke="#d97706"/>
    <text x="705" y="102" text-anchor="middle" font-size="18" fill="#92400e">추정량의 경험적 분포</text>
    <text x="705" y="126" text-anchor="middle" font-size="16" fill="#92400e">표준오차·구간 추정</text>
    <line x1="220" y1="75" x2="300" y2="57" stroke="#64748b" stroke-width="3"/>
    <line x1="220" y1="75" x2="300" y2="117" stroke="#64748b" stroke-width="3"/>
    <line x1="220" y1="75" x2="300" y2="177" stroke="#64748b" stroke-width="3"/>
    <line x1="460" y1="57" x2="610" y2="92" stroke="#64748b" stroke-width="3"/>
    <line x1="460" y1="117" x2="610" y2="108" stroke="#64748b" stroke-width="3"/>
    <line x1="460" y1="177" x2="610" y2="124" stroke="#64748b" stroke-width="3"/>
  </svg>
  <figcaption>부트스트랩은 원표본에서 복원추출한 재표집 표본들의 추정량 분포로 불확실성을 근사한다.</figcaption>
</figure>

## 22.0.5 이 장의 핵심 질문

이 장에서는 네 가지 질문을 중심으로 논의를 전개한다.

1. 표준 부트스트랩은 어떤 정칙성 조건 아래에서 타당한가.
2. 어떤 추정량에서 왜 실패하는가.
3. 실패하는 경우에는 subsampling이나 \(m\)-out-of-\(n\) bootstrap 같은 대안이 왜 필요한가.
4. 이중 기계학습이나 복잡한 정책평가 절차에서는 어떤 형태의 재표집이 적절한가.

## 22.0.6 정책평가 연구자가 기억할 점

부트스트랩은 편리하지만, 추정량의 구조를 이해하지 않은 채 기계적으로 적용해서는 안 된다. 특히 정책평가에서는 다음을 항상 점검해야 한다.

- 추정량이 정칙적인가
- 튜닝 파라미터 선택이 포함되어 있는가
- 매칭, trimming, threshold처럼 이산적 단계가 있는가
- cluster bootstrap이나 block bootstrap이 필요한 자료구조인가

이 장의 목표는 부트스트랩을 포기하자는 것이 아니다. 오히려 **언제 믿을 수 있고 언제 경계해야 하는지**를 분명히 해, 정책효과의 불확실성을 더 정직하게 보고하도록 만드는 데 있다.
