---
title: 8장. 외적 타당도, 내적 타당도, 그리고 일반화의 문제
description: 실험에서 식별된 효과를 다른 사람, 다른 장소, 다른 제도 환경으로 옮겨 읽을 때 어떤 가정과 한계가 생기는지를 정리한다.
---

# 7?. ?? ???, ?? ???, ??? ???? ??
7장까지의 논의는 주로 내적 타당도에 집중되어 있었다. 즉, 주어진 연구 표본 안에서 관찰된 차이를 인과효과로 해석할 수 있는가가 핵심 질문이었다. 그러나 정책평가의 실제 관심은 거의 언제나 그다음 단계로 이어진다. “이 실험 결과를 다른 지역에도 적용할 수 있는가?”, “이 표본에서 식별된 효과를 전국 정책효과로 읽어도 되는가?”, “실험실이나 현장실험의 결과가 실제 행정 프로그램으로 확대될 때도 유지되는가?”

이 질문이 바로 외적 타당도(external validity)의 문제다. 내적 타당도가 “이 비교가 인과적인가”를 묻는다면, 외적 타당도는 “그 인과효과가 어디까지 유효한가”를 묻는다. 따라서 외적 타당도는 내적 타당도의 대체물이 아니라, 그 위에 추가로 얹히는 해석 층위다.

정책평가에서는 이 둘이 종종 긴장 관계에 놓인다. 엄격한 참여 기준, 통제된 환경, 제한된 실행 조건은 표본 안의 비교가능성을 높여 내적 타당도를 강화한다. 하지만 바로 그 이유 때문에 결과를 더 넓은 현실 세계로 일반화하기는 어려워질 수 있다. 반대로 실제 행정 환경에 가까운 연구는 적용 가능성은 높지만, 식별은 더 어려워질 수 있다.

이 장은 이 긴장을 이해하고 다루는 방법을 정리한다. 핵심 관심사는 세 가지다. 첫째, 내적 타당도와 외적 타당도는 왜 동시에 중요하면서도 서로 다른 질문에 답하는가. 둘째, 연구 표본과 목표 모집단이 다를 때 어떤 해석 오류가 생기는가. 셋째, 일반화와 transportability는 어떤 가정 위에서 가능한가.

\[
\mathrm{SATE} = \mathbb{E}[Y(1)-Y(0)\mid S=1], \qquad
\mathrm{TATE} = \mathbb{E}[Y(1)-Y(0)\mid S=0].
\]

외적 타당도는 결국 이 두 값의 차이가 왜 생기며, 어떤 조건에서 메울 수 있는가를 다루는 문제라고 볼 수 있다.

## 시각화: 식별된 효과에서 정책효과로

<svg viewBox="0 0 880 280" role="img" aria-label="연구 표본에서 식별된 효과를 목표 모집단으로 일반화하는 과정" class="chapter-figure">
  <style>
    .box { fill: #f8fafc; stroke: #334155; stroke-width: 2; rx: 14; ry: 14; }
    .soft { fill: #eef6ff; stroke: #2563eb; stroke-width: 2; rx: 14; ry: 14; }
    .warn { fill: #fff7ed; stroke: #c2410c; stroke-width: 2; rx: 14; ry: 14; }
    .txt { font: 16px 'Noto Sans KR', sans-serif; fill: #111827; }
    .small { font: 14px 'Noto Sans KR', sans-serif; fill: #475569; }
    .arrow { stroke: #4b5563; stroke-width: 2.4; fill: none; marker-end: url(#m8a); }
  </style>
  <defs>
    <marker id="m8a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
      <path d="M0,0 L10,5 L0,10 z" fill="#4b5563"></path>
    </marker>
  </defs>
  <rect class="soft" x="50" y="90" width="200" height="100"></rect>
  <text class="txt" x="150" y="128" text-anchor="middle">연구 표본</text>
  <text class="small" x="150" y="153" text-anchor="middle">무작위화로 내적 타당도 확보</text>

  <rect class="box" x="340" y="90" width="200" height="100"></rect>
  <text class="txt" x="440" y="128" text-anchor="middle">식별된 효과</text>
  <text class="small" x="440" y="153" text-anchor="middle">보통 SATE 또는 ITT</text>

  <rect class="warn" x="630" y="90" width="200" height="100"></rect>
  <text class="txt" x="730" y="128" text-anchor="middle">목표 모집단</text>
  <text class="small" x="730" y="153" text-anchor="middle">TATE 또는 PATE로의 일반화</text>

  <path class="arrow" d="M250 140 L340 140"></path>
  <path class="arrow" d="M540 140 L630 140"></path>
</svg>

이 장의 네 절은 다음 흐름으로 이어진다.

1. `8.1` 내적 타당도와 외적 타당도의 긴장
2. `8.2` 연구 표본과 목표 모집단의 불일치
3. `8.3` 실험 결과의 일반화와 transportability
4. `8.4` 현장실험과 자연실험의 위치

이 장을 읽고 나면, “좋은 실험”이 자동으로 “좋은 정책지식”을 뜻하지는 않으며, 연구결과를 어디까지 옮겨 말할 수 있는가는 별도의 가정과 증거를 필요로 한다는 점이 분명해질 것이다.
