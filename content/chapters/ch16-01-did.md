---
title: 16.1 DiD의 기본 직관과 2x2 설계
description: DiD의 출발점은 2집단 2시점 비교다. 이 절은 변화의 차이라는 기본 아이디어, ATT 해석, 정책평가에서 왜 이 설계가 널리 쓰이는지를 설명한다.
---

# 16.1 DiD의 기본 직관과 2x2 설계

DiD를 처음 이해할 때는 가장 단순한 **2집단 2시점(2x2)** 구조에서 출발하는 것이 좋다. 하나의 처치군, 하나의 비교군, 하나의 사전시점, 하나의 사후시점이 있을 때 DiD는 “변화의 차이”를 계산한다.

## 2x2 DiD 추정량

\[
\tau_{DiD}
=
(\bar Y_{1,post}-\bar Y_{1,pre})
-
(\bar Y_{0,post}-\bar Y_{0,pre})
\]

첫 번째 괄호는 처치군의 변화이고, 두 번째 괄호는 비교군의 변화다. 처치군 변화에서 비교군 변화를 빼면 공통된 거시충격이나 자연적 추세를 어느 정도 제거할 수 있다는 것이 DiD의 직관이다.

## 직관적으로는 무엇을 하는가

예를 들어 어느 지역에만 청년고용 보조금이 도입되었다고 하자. 정책 후 취업률이 5%p 상승했다고 해서 그 전체를 정책효과로 읽을 수는 없다. 경기회복 때문에 비교지역도 2%p 상승했을 수 있기 때문이다. 이때 DiD는 “정책지역은 5%p, 비교지역은 2%p 올랐으니, 순효과는 3%p”라고 해석한다.

즉 DiD는 처치군의 변화를 있는 그대로 읽지 않고, 비교군의 자연변화를 기준선으로 삼아 다시 조정한다.

## 시각적으로 보면 무엇이 일어나는가

아래 그림은 2x2 DiD의 핵심 직관을 단순화해서 보여준다. 비교군은 정책이 없을 때의 자연적 변화 경로를 나타내고, 처치군은 정책 이후 그 경로에서 추가로 벌어진 만큼이 정책효과로 읽힌다.

<figure class="chapter-figure">
  <svg viewBox="0 0 760 360" role="img" aria-labelledby="did-basic-visual-title did-basic-visual-desc">
    <title id="did-basic-visual-title">Difference-in-Differences 기본 시각화</title>
    <desc id="did-basic-visual-desc">사전과 사후 시점에서 비교군과 처치군의 결과 수준을 선으로 보여주고, 사후 시점에서 두 선 사이의 추가 격차를 DID 효과로 설명하는 도식이다.</desc>
    <defs>
      <marker id="arrowhead-did" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
        <polygon points="0 0, 10 4, 0 8" fill="#2f5d50"></polygon>
      </marker>
      <marker id="arrowhead-did-gray" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
        <polygon points="0 0, 10 4, 0 8" fill="#7b8794"></polygon>
      </marker>
    </defs>

    <rect x="0" y="0" width="760" height="360" fill="#fbfaf4"></rect>

    <line x1="90" y1="300" x2="700" y2="300" stroke="#293241" stroke-width="2"></line>
    <line x1="90" y1="300" x2="90" y2="55" stroke="#293241" stroke-width="2"></line>

    <text x="705" y="306" font-size="16" fill="#293241">시간</text>
    <text x="38" y="66" font-size="16" fill="#293241">결과</text>

    <line x1="220" y1="300" x2="220" y2="90" stroke="#c9ced6" stroke-dasharray="6 6"></line>
    <line x1="560" y1="300" x2="560" y2="90" stroke="#c9ced6" stroke-dasharray="6 6"></line>

    <text x="195" y="326" font-size="16" fill="#293241">사전</text>
    <text x="535" y="326" font-size="16" fill="#293241">사후</text>

    <circle cx="220" cy="215" r="6" fill="#506d84"></circle>
    <circle cx="560" cy="180" r="6" fill="#506d84"></circle>
    <line x1="220" y1="215" x2="560" y2="180" stroke="#506d84" stroke-width="4"></line>
    <text x="575" y="183" font-size="16" fill="#506d84">비교군</text>

    <circle cx="220" cy="205" r="6" fill="#d06b36"></circle>
    <circle cx="560" cy="125" r="6" fill="#d06b36"></circle>
    <line x1="220" y1="205" x2="560" y2="125" stroke="#d06b36" stroke-width="4"></line>
    <text x="575" y="128" font-size="16" fill="#d06b36">처치군 관측값</text>

    <line x1="220" y1="205" x2="560" y2="170" stroke="#7b8794" stroke-width="3" stroke-dasharray="10 7"></line>
    <text x="332" y="160" font-size="15" fill="#7b8794">정책이 없었을 때의 반사실 경로</text>

    <line x1="560" y1="170" x2="560" y2="125" stroke="#2f5d50" stroke-width="4" marker-end="url(#arrowhead-did)"></line>
    <text x="575" y="152" font-size="15" fill="#2f5d50">DID 효과</text>

    <line x1="250" y1="205" x2="250" y2="215" stroke="#7b8794" stroke-width="3" marker-end="url(#arrowhead-did-gray)"></line>
    <text x="258" y="214" font-size="14" fill="#7b8794">사전에는 수준 차이가 있을 수 있음</text>

    <rect x="102" y="28" width="250" height="42" rx="8" fill="#fff3e8" stroke="#e6c4a8"></rect>
    <text x="116" y="54" font-size="15" fill="#7a3f18">핵심: 처치군 변화 전체가 아니라 비교군 변화만큼을 뺀 추가 변화</text>
  </svg>
  <figcaption>2x2 DID의 기본 아이디어: 사후 시점에서 처치군 관측값과 반사실 경로의 차이가 정책효과로 읽힌다.</figcaption>
</figure>

이 그림에서 중요한 점은 두 집단의 **출발 수준이 완전히 같을 필요는 없다는 것**이다. DiD는 출발점 차이 자체보다, 정책이 없었을 때 두 집단의 **변화 방향과 변화 폭**이 얼마나 비슷했을지를 더 중요하게 본다.

## 잠재결과 관점에서의 해석

잠재결과 표기로 쓰면, 2x2 DiD는 보통 다음과 같은 평균 처치효과를 겨냥한다.

\[
ATT
=
E[Y_{post}(1)-Y_{post}(0)\mid G=1].
\]

여기서 핵심은 \(Y_{post}(0)\), 즉 처치군이 정책을 받지 않았더라면 사후에 어떤 결과를 보였을지를 직접 관찰할 수 없다는 점이다. DiD는 이 반사실을 비교군의 변화 경로를 통해 근사한다.

## 정책평가 사례

DiD는 다음 같은 상황에서 특히 직관적이다.

- 어떤 주에서만 최저임금이 인상된 경우
- 특정 연도부터 일부 학교에만 재정지원이 확대된 경우
- 특정 지역에만 환경규제가 강화된 경우
- 보험급여 확대가 일부 인구집단에만 우선 적용된 경우

이런 경우 연구자는 “정책도입 전후 변화”와 “도입되지 않은 집단의 변화”를 비교하여 효과를 추정한다.

## DiD의 장점

- 수준 차이가 아니라 변화 차이를 보므로, 고정된 집단 간 차이에 어느 정도 강하다.
- 정책평가 맥락과 잘 맞는다.
- 회귀식으로 확장하기 쉽고 패널자료와 잘 결합된다.
- event-study, staggered adoption, synthetic DiD 같은 확장으로 이어질 수 있다.

## 하지만 2x2 DiD는 출발점일 뿐이다

현실의 연구는 보통 이보다 훨씬 복잡하다.

- 시점이 두 개보다 많다.
- 정책 도입 시점이 집단마다 다르다.
- 효과가 즉시 나타나지 않을 수 있다.
- 정책 기대효과 때문에 사전행동이 달라질 수 있다.

따라서 2x2의 직관을 이해한 뒤에는, 이를 패널 회귀와 동태적 분석으로 옮겨가는 과정이 필요하다.

## 정리

DiD의 출발점은 매우 단순하다. 처치군의 변화에서 비교군의 변화를 뺀다. 그러나 바로 그 단순한 구조 덕분에 정책평가에서 강력한 설계가 된다. 다음 절에서는 이 아이디어를 회귀표현과 패널자료 언어로 일반화한다.
