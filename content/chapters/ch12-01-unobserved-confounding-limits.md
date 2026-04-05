---
title: 12장. 간섭, 집행, 집계 수준의 문제
description: 개인이 서로 독립적이지 않고, 정책이 균일하게 구현되지 않으며, 자료 수준이 섞일 때 인과추론이 어떻게 어려워지는지를 다룬다.
---

# 12장. 간섭, 집행, 집계 수준의 문제

지금까지의 많은 논의는 암묵적으로 한 단위의 처치가 다른 단위의 결과에 영향을 주지 않고, 같은 정책은 모든 사람에게 동일한 형태로 전달되며, 자료의 분석 수준과 정책 질문의 수준이 일치한다고 가정해 왔다. 그러나 실제 정책세계는 그렇지 않다. 한 사람의 백신 접종은 다른 사람의 감염위험을 바꾸고, 같은 복지정책도 지자체와 담당자에 따라 다르게 집행되며, 개인수준 자료가 없어서 지역 평균만 가지고 결론을 내리는 경우도 많다.

이 장은 바로 그런 `현실의 상호의존성`을 다룬다. 이는 단순한 기술적 예외가 아니라, 인과효과의 정의 자체를 바꾸는 문제일 수 있다.

## 이 장의 구조

1. `12.1`에서는 간섭(interference)과 spillover를 설명한다.
2. `12.2`에서는 정책집행의 이질성과 implementation heterogeneity를 다룬다.
3. `12.3`에서는 집계자료, 생태학적 오류, 다수준 맥락을 설명한다.

## 시각화: 고립된 개인이 아니라 연결된 단위들

<svg viewBox="0 0 860 280" role="img" aria-label="간섭과 집행, 집계수준 문제의 개요" class="chapter-figure">
  <style>
    .node { fill: #f8fafc; stroke: #334155; stroke-width: 2; rx: 12; ry: 12; }
    .txt { font: 16px 'Noto Sans KR', sans-serif; fill: #111827; }
    .small { font: 14px 'Noto Sans KR', sans-serif; fill: #475569; }
    .arrow { stroke: #4b5563; stroke-width: 2.2; fill: none; marker-end: url(#m12a); }
  </style>
  <defs>
    <marker id="m12a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#4b5563"></path>
    </marker>
  </defs>
  <rect class="node" x="80" y="100" width="130" height="70"></rect>
  <text class="txt" x="145" y="142" text-anchor="middle">개인 A의 처치</text>
  <rect class="node" x="365" y="40" width="130" height="70"></rect>
  <text class="txt" x="430" y="82" text-anchor="middle">개인 B의 결과</text>
  <rect class="node" x="365" y="160" width="130" height="70"></rect>
  <text class="txt" x="430" y="202" text-anchor="middle">기관의 집행 방식</text>
  <rect class="node" x="650" y="100" width="130" height="70"></rect>
  <text class="txt" x="715" y="142" text-anchor="middle">지역 평균 자료</text>
  <path class="arrow" d="M210 120 L365 85"></path>
  <path class="arrow" d="M210 150 L365 185"></path>
  <path class="arrow" d="M495 135 L650 135"></path>
</svg>

이 장의 메시지는 분명하다. 정책효과는 종종 개인의 고립된 반응이 아니라, 네트워크·제도·집계수준이라는 맥락 속에서 형성된다. 따라서 그 맥락을 무시하면 효과를 잘못 정의하거나 잘못 해석할 수 있다.
