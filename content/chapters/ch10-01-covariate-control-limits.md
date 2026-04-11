---
title: 8장. 측정, 관측, 결측의 문제
description: This chapter explains how measurement error, recording error, and missingness distort observational data before causal analysis even begins.
---

# 8장. 측정, 관측, 결측의 문제

관측자료의 가장 현실적인 문제는 교란을 모두 통제하지 못한다는 점만이 아니다. 더 앞선 단계에서, 우리가 손에 쥐고 있는 데이터 자체가 현실을 정확히 반영하지 않을 수 있다. 처치가 잘못 기록되기도 하고, 결과가 부정확하게 측정되기도 하며, 일부 응답은 빠지고, 행정자료는 특정 집단을 체계적으로 놓치기도 한다. 이 장은 이러한 `데이터 생성 과정(data-generating and data-recording process)` 자체가 인과추론을 어떻게 흔드는지를 다룬다.

인과효과를 \(Y(1)-Y(0)\) 로 정의하더라도 실제 분석에서 보는 것은 대개 관측된 처치 \(D^\*\), 관측된 결과 \(Y^\*\), 관측된 공변량 \(X^\*\) 이다. 따라서 분석은 본질적으로 다음과 같은 층위를 갖는다.

\[
(D, Y, X) \longrightarrow (D^\*, Y^\*, X^\*) \longrightarrow \text{estimator}.
\]

만약 첫 번째 화살표에서 왜곡이 생기면, 그 뒤의 회귀·매칭·가중치 기법이 아무리 정교해도 왜곡된 자료를 바탕으로 결론을 내릴 수밖에 없다. 그래서 측정오차와 결측은 “부차적 통계 문제”가 아니라 인과식별과 해석을 직접 흔드는 문제다.

## 왜 이 장이 필요한가

정책평가와 행정자료 연구에서는 다음과 같은 상황이 아주 흔하다.

1. 실제 프로그램 참여 여부와 행정상 등록 여부가 다르다.
2. 소득, 건강, 교육성과 같은 핵심 결과가 자기보고(self-report)로 측정된다.
3. 패널조사에서 특정 집단이 더 많이 이탈한다.
4. 온라인 플랫폼 자료는 앱을 사용하는 사람만 관찰한다.

이때 분석가는 단순히 “데이터가 완벽하지 않다”는 수준을 넘어서, **오류가 어떤 구조를 가지는지**, **그 오류가 처치·결과와 독립적인지**, **보정 가능한지**를 판단해야 한다.

## 이 장의 구조

10장은 다음 세 절로 구성된다.

1. `10.1`에서는 측정오차와 분류오차가 어떤 편의를 만드는지 설명한다.
2. `10.2`에서는 결측자료를 MCAR, MAR, MNAR로 구분하고 각각의 의미를 정리한다.
3. `10.3`에서는 다중대체, 가중치, 보정행렬, 민감도 분석 같은 대응 전략을 다룬다.

## 시각화: 현실에서 분석까지의 관측 과정

<svg viewBox="0 0 900 290" role="img" aria-label="현실의 변수에서 관측된 변수와 추정량으로 이어지는 과정" class="chapter-figure">
  <style>
    .box { fill: #f8fafc; stroke: #334155; stroke-width: 2; rx: 14; ry: 14; }
    .warn { fill: #fff7ed; stroke: #c2410c; stroke-width: 2; rx: 14; ry: 14; }
    .txt { font: 16px 'Noto Sans KR', sans-serif; fill: #111827; }
    .small { font: 14px 'Noto Sans KR', sans-serif; fill: #475569; }
    .arrow { stroke: #4b5563; stroke-width: 2.4; fill: none; marker-end: url(#m10a); }
  </style>
  <defs>
    <marker id="m10a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#4b5563"></path>
    </marker>
  </defs>
  <rect class="box" x="40" y="90" width="210" height="110"></rect>
  <text class="txt" x="145" y="128" text-anchor="middle">현실의 변수</text>
  <text class="small" x="145" y="154" text-anchor="middle">\(D, Y, X\)</text>
  <text class="small" x="145" y="178" text-anchor="middle">실제 처치, 결과, 공변량</text>

  <rect class="warn" x="345" y="90" width="210" height="110"></rect>
  <text class="txt" x="450" y="128" text-anchor="middle">관측된 변수</text>
  <text class="small" x="450" y="154" text-anchor="middle">\(D^\*, Y^\*, X^\*\)</text>
  <text class="small" x="450" y="178" text-anchor="middle">오측정, 분류오차, 결측 가능</text>

  <rect class="box" x="650" y="90" width="210" height="110"></rect>
  <text class="txt" x="755" y="128" text-anchor="middle">분석 결과</text>
  <text class="small" x="755" y="154" text-anchor="middle">회귀, 매칭, 가중치, DID</text>
  <text class="small" x="755" y="178" text-anchor="middle">모두 관측된 자료에 의존</text>

  <path class="arrow" d="M250 145 L345 145"></path>
  <path class="arrow" d="M555 145 L650 145"></path>
</svg>

이 그림은 중요한 사실을 보여준다. 인과추정량은 대개 관측된 자료에만 접근할 수 있으므로, 자료화 과정의 왜곡을 따로 모델링하지 않으면 `잘못 측정된 현실` 위에 정교한 분석을 얹게 된다. 따라서 이 장은 13장 이후의 방법론을 배우기 전에, 우리가 다루는 자료 자체가 어떤 한계를 가지는지 분명히 인식하게 해 준다.
