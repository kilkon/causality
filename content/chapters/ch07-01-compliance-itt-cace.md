---
title: 7장. 순응, ITT, CACE와 실험의 내적 타당도
description: 무작위 배정이 실제 정책현장에서 완전하게 구현되지 않을 때, 실험의 내적 타당도를 어떻게 해석하고 지켜야 하는지를 정리한다.
---

# 7장. 순응, ITT, CACE와 실험의 내적 타당도

6장에서 본 무작위화는 처치와 잠재결과 사이의 체계적 연관을 끊어 주기 때문에 실험의 내적 타당도를 세우는 가장 강력한 장치다. 그러나 실제 정책실험에서는 배정받은 사람이 처치를 거부하기도 하고, 통제군이 프로그램에 우회적으로 접근하기도 하며, 추적조사 중 일부가 이탈하기도 한다. 이런 문제는 무작위화 자체를 무효화한다기보다, **무작위로 배정된 것**과 **실제로 받은 것**을 구분해 읽어야 한다는 점을 보여준다.

이 장은 바로 그 지점을 다룬다. 핵심 질문은 다음과 같다. 첫째, 정책효과를 말할 때 우리는 `배정의 효과`를 말하는가, 아니면 `실제 수령의 효과`를 말하는가. 둘째, 부분 순응과 이탈이 있을 때도 무작위화가 제공하는 내적 타당도는 어디까지 유지되는가. 셋째, 연구자는 어떤 추정량을 보고해야 하며, 어떤 추가 가정이 들어가는지를 어떻게 투명하게 설명해야 하는가.

내적 타당도 관점에서 보면, 순응(compliance) 문제는 단순한 자료 정리 이슈가 아니다. 이는 “무작위화가 식별해 주는 대상이 무엇인가”를 다시 묻는 문제다. 배정 \(Z\) 는 무작위이지만 실제 처치 수령 \(D\) 는 그렇지 않을 수 있다. 따라서 관찰자료는 대체로 다음 두 층위를 가진다.

\[
Z_i \in \{0,1\}, \qquad D_i \in \{0,1\}, \qquad Y_i = Y_i(D_i).
\]

여기서 \(Z_i\) 는 연구자가 설계한 처치 배정, \(D_i\) 는 실제 수령 여부, \(Y_i\) 는 결과다. 완전 순응이면 \(D_i=Z_i\) 이므로 문제가 단순하다. 하지만 부분 순응에서는 \(D_i \neq Z_i\) 인 사례가 생기므로, 무작위화가 직접 식별하는 것은 우선

\[
\text{ITT} = E[Y_i \mid Z_i=1] - E[Y_i \mid Z_i=0]
\]

이다. 즉 **배정의 효과**가 가장 먼저 식별된다. 반면 실제 수령의 효과를 말하려면 추가 구조가 필요하고, 이때 도구변수 해석과 단조성 가정이 등장한다.

다르게 말하면, 이 장은 내적 타당도를 “실험이 망가졌는가 아닌가”의 이분법으로 보지 않는다. 오히려 다음처럼 더 정밀하게 본다.

1. 무작위 배정 자체는 여전히 보존되었는가.
2. 그렇다면 ITT는 여전히 강한 내적 타당도를 가지는가.
3. 실제 수령 효과(CACE/LATE)까지 해석하려면 어떤 추가 가정이 필요한가.
4. 이탈자와 무응답은 배정의 무작위성을 약화시키는가, 아니면 결과 관측의 선택편의를 만드는가.

아래 그림은 이 장의 전체 구조를 요약한다.

<svg viewBox="0 0 860 280" role="img" aria-label="무작위 배정에서 순응 문제와 내적 타당도의 관계" class="chapter-figure">
  <style>
    .box { fill: #f7f8fb; stroke: #2f4f4f; stroke-width: 2; rx: 14; ry: 14; }
    .accent { fill: #fff4df; stroke: #b7791f; stroke-width: 2; rx: 14; ry: 14; }
    .warn { fill: #fdecec; stroke: #b83232; stroke-width: 2; rx: 14; ry: 14; }
    .txt { font: 16px 'Noto Sans KR', sans-serif; fill: #1f2937; }
    .small { font: 14px 'Noto Sans KR', sans-serif; fill: #374151; }
    .arrow { stroke: #4b5563; stroke-width: 2.4; fill: none; marker-end: url(#m); }
  </style>
  <defs>
    <marker id="m" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#4b5563"></path>
    </marker>
  </defs>
  <rect class="box" x="40" y="90" width="170" height="90"></rect>
  <text class="txt" x="125" y="126" text-anchor="middle">무작위 배정</text>
  <text class="small" x="125" y="151" text-anchor="middle">\(Z\) is randomized</text>

  <rect class="accent" x="260" y="90" width="170" height="90"></rect>
  <text class="txt" x="345" y="126" text-anchor="middle">부분 순응</text>
  <text class="small" x="345" y="151" text-anchor="middle">\(D \neq Z\) 가능</text>

  <rect class="box" x="480" y="30" width="160" height="90"></rect>
  <text class="txt" x="560" y="66" text-anchor="middle">ITT</text>
  <text class="small" x="560" y="91" text-anchor="middle">배정의 효과</text>

  <rect class="box" x="480" y="160" width="160" height="90"></rect>
  <text class="txt" x="560" y="196" text-anchor="middle">CACE / LATE</text>
  <text class="small" x="560" y="221" text-anchor="middle">순응자에 대한 수령 효과</text>

  <rect class="warn" x="690" y="90" width="130" height="90"></rect>
  <text class="txt" x="755" y="126" text-anchor="middle">이탈 · 무응답</text>
  <text class="small" x="755" y="151" text-anchor="middle">추적 손실과 선택</text>

  <path class="arrow" d="M210 135 L260 135"></path>
  <path class="arrow" d="M430 115 L480 75"></path>
  <path class="arrow" d="M430 155 L480 205"></path>
  <path class="arrow" d="M640 135 L690 135"></path>
</svg>

이 그림의 의미는 분명하다. 무작위 배정은 내적 타당도의 출발점이지만, 부분 순응이 생기면 연구자가 보고하는 효과의 의미가 갈라진다. ITT는 여전히 설계 기반 추정량으로서 매우 강한 지위를 갖는다. 반면 CACE/LATE는 “배정이 실제 수령을 움직인 사람들”이라는 국소 집단에 대한 효과이므로, 추가 가정과 해석상의 절제가 필요하다. 그리고 이탈자(attrition)와 무응답은 표본선택 문제를 만들어 실험의 내적 타당도를 다시 위협할 수 있다.

따라서 7장의 네 절은 다음 질문에 순차적으로 답한다.

1. 완전 순응과 부분 순응을 구분할 때 왜 `배정`과 `수령`을 따로 봐야 하는가.
2. ITT와 CACE/LATE는 각각 어떤 정책질문에 답하는가.
3. 무작위 배정을 왜 도구변수로 읽을 수 있으며, 단조성은 왜 필요한가.
4. 이탈과 무응답을 어떻게 다루어야 실험의 신뢰성을 유지할 수 있는가.

이 장을 읽고 나면, 무작위실험의 내적 타당도는 단순히 “랜덤화했으니 끝”이 아니라, **배정-수령-관측의 세 층위를 구분하여 해석하는 능력** 위에 놓여 있음을 이해하게 된다.
