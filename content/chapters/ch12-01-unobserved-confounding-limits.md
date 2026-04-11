---
title: 12. 간섭, 집행, 집계 수준의 문제
description: This chapter explains how spillovers, implementation heterogeneity, and aggregation change the meaning of causal effects.
---

# 10?. ??, ??, ?? ??? ??
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
