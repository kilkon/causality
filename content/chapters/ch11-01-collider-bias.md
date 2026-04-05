---
title: 11. 시간, 동태성, 역인과성
description: This chapter focuses on temporal ordering, simultaneity, dynamic treatment paths, and reverse causality in observational data.
---

# 11. 시간, 동태성, 역인과성

관측자료 분석에서 가장 자주 놓치는 조건은 시간 순서다. 인과추론에서 원인은 결과보다 앞서 있어야 하지만, 현실의 데이터는 종종 특정 시점의 단면(snapshot)만 제공하거나, 처치와 결과가 반복적으로 상호작용한 뒤 남은 한 장면만 보여 준다. 이때 상관을 보았다고 해서 방향을 곧바로 확정할 수는 없다.

예를 들어 소득과 건강은 서로 영향을 주고, 교육과 기대도 함께 변하며, 정책 참여와 노동시장 성과는 여러 시점에 걸쳐 누적적으로 연결된다. 따라서 “무엇이 먼저였는가”와 “효과가 즉시 나타나는가 아니면 지연되는가”를 구분하지 않으면, 관측자료 분석은 쉽게 역인과성(reverse causality)이나 동시성(simultaneity)의 함정에 빠진다.

## 왜 시간 문제가 중요한가

인과효과를 잠재결과로 쓰면

\[
Y_t(d)
\]

는 시점 \(t\) 에서 처치 상태 \(d\) 아래 가능한 결과를 뜻한다. 하지만 실제 정책은 대개 단일 시점 처치가 아니라,

\[
D_1, D_2, \dots, D_t
\]

처럼 시간이 흐르며 반복되거나 강도가 누적된다. 따라서 분석도 단순한 정태적 비교가 아니라, 시간구조를 반영한 질문이어야 한다.

## 이 장의 구조

1. `11.1`에서는 시간 순서와 역인과성의 문제를 다룬다.
2. `11.2`에서는 사전값 통제, 동시성, 상호결정 구조를 설명한다.
3. `11.3`에서는 누적처치와 지연효과 같은 동태적 효과를 다룬다.

## 시각화: 정태적 상관과 동태적 인과

<svg viewBox="0 0 900 280" role="img" aria-label="정태적 상관과 동태적 인과구조의 차이" class="chapter-figure">
  <style>
    .panel { fill: #f8fafc; stroke: #334155; stroke-width: 2; rx: 12; ry: 12; }
    .node { fill: white; stroke: #475569; stroke-width: 1.8; rx: 10; ry: 10; }
    .txt { font: 15px 'Noto Sans KR', sans-serif; fill: #111827; }
    .small { font: 13px 'Noto Sans KR', sans-serif; fill: #475569; }
    .arrow { stroke: #4b5563; stroke-width: 2.1; fill: none; marker-end: url(#m11a); }
  </style>
  <defs>
    <marker id="m11a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#4b5563"></path>
    </marker>
  </defs>
  <rect class="panel" x="25" y="35" width="380" height="210"></rect>
  <text class="txt" x="215" y="65" text-anchor="middle">정태적 단면 비교</text>
  <rect class="node" x="110" y="115" width="90" height="50"></rect>
  <text class="txt" x="155" y="146" text-anchor="middle">\(D\)</text>
  <rect class="node" x="250" y="115" width="90" height="50"></rect>
  <text class="txt" x="295" y="146" text-anchor="middle">\(Y\)</text>
  <path class="arrow" d="M200 140 L250 140"></path>
  <text class="small" x="215" y="205" text-anchor="middle">관측 시점 하나만 보면 방향이 불분명할 수 있다</text>

  <rect class="panel" x="495" y="35" width="380" height="210"></rect>
  <text class="txt" x="685" y="65" text-anchor="middle">동태적 시간 구조</text>
  <rect class="node" x="530" y="105" width="80" height="45"></rect>
  <text class="txt" x="570" y="133" text-anchor="middle">\(D_{t-1}\)</text>
  <rect class="node" x="650" y="105" width="80" height="45"></rect>
  <text class="txt" x="690" y="133" text-anchor="middle">\(Y_t\)</text>
  <rect class="node" x="770" y="105" width="80" height="45"></rect>
  <text class="txt" x="810" y="133" text-anchor="middle">\(D_t\)</text>
  <path class="arrow" d="M610 128 L650 128"></path>
  <path class="arrow" d="M730 128 L770 128"></path>
  <path class="arrow" d="M690 150 Q 690 205 570 205 Q 525 205 525 150" style="stroke:#4b5563;stroke-width:2.1;fill:none;marker-end:url(#m11a)"></path>
  <text class="small" x="685" y="220" text-anchor="middle">과거 처치가 현재 결과를 바꾸고, 현재 결과가 다음 처치에 영향을 줄 수 있다</text>
</svg>

이 장의 핵심 메시지는 단순하다. 시간 구조를 잃어버리면 관측자료에서 인과방향은 쉽게 뒤집히거나 섞인다. 그래서 이후 DID, 패널모형, 동태적 정책평가 기법들이 왜 필요한지도 이 장에서 더 잘 이해할 수 있다.
