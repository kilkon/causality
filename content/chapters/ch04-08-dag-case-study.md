---
title: 4.8 DAG를 이용한 편향 가능성 분석 사례
description: 이 절은 하나의 실제 연구가설을 가지고 DAG로 교란변수, 매개변수, 충돌변수 가능성을 어떻게 점검하는지 보여준다.
---

# 4.8 DAG를 이용한 편향 가능성 분석 사례

앞 절들에서는 DAG의 기본 규칙, back-door 경로, 선택편의와 충돌편의를 개념적으로 살펴보았다. 하지만 실제 연구에서는 “이 변수는 통제해야 하는가, 아니면 오히려 통제하면 안 되는가”라는 질문이 훨씬 더 중요하다. 이 절에서는 하나의 구체적 연구가설을 가지고, DAG가 실제로 어떤 판단 도구가 되는지를 보여준다.

## 사례 1. 연민적 공감 역량과 행정부담 관용 태도

연구가설을 다음처럼 정리해 보자.

> 연민적 공감 역량이 높을수록, 공무원의 행정부담에 대한 관용적 태도는 낮아진다.

여기서

- \(X\): 연민적 공감 역량
- \(Y\): 행정부담에 대한 관용 태도

를 뜻한다. 관용 태도가 높다는 것은 시민에게 부과되는 절차적, 학습적, 심리적 부담을 어느 정도 정당하거나 수용 가능한 것으로 보는 태도다. 따라서 가설은 보통

\[
X \uparrow \;\Rightarrow\; Y \downarrow
\]

의 방향을 가진다.

## 가장 단순한 이론적 DAG

가장 단순하게는 다음처럼 그릴 수 있다.

<figure class="chapter-figure">
  <svg viewBox="0 0 620 180" role="img" aria-label="연민적 공감 역량과 행정부담 관용 태도의 단순 DAG">
    <rect x="70" y="60" width="180" height="60" rx="16" fill="#e8f2ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="160" y="87" text-anchor="middle" font-size="18" fill="#1e3a5f">X</text>
    <text x="160" y="108" text-anchor="middle" font-size="14" fill="#1e3a5f">연민적 공감 역량</text>

    <rect x="370" y="60" width="180" height="60" rx="16" fill="#fff4e6" stroke="#d97706" stroke-width="2"/>
    <text x="460" y="87" text-anchor="middle" font-size="18" fill="#7c3d00">Y</text>
    <text x="460" y="108" text-anchor="middle" font-size="14" fill="#7c3d00">행정부담 관용 태도</text>

    <line x1="250" y1="90" x2="370" y2="90" stroke="#374151" stroke-width="3"/>
    <polygon points="370,90 355,82 355,98" fill="#374151"/>
  </svg>
  <figcaption>가장 단순한 가설 구조: 연민적 공감 역량이 행정부담 관용 태도에 영향을 준다고 보는 DAG.</figcaption>
</figure>

하지만 실제 연구에서는 이 DAG만으로는 거의 항상 부족하다. 왜냐하면 연민적 공감과 행정부담 태도는 모두 개인의 가치관, 조직환경, 직무경험의 영향을 받을 가능성이 크기 때문이다.

## 현실적인 DAG: 공통원인(confounder) 포함

보다 현실적인 DAG를 생각하면 다음과 같은 공통원인이 들어올 수 있다.

- \(Z_1\): 공공봉사동기(public service motivation)
- \(Z_2\): 복지관, 시민책임관, 형평성 규범, 이념
- \(Z_3\): 현장 민원 접촉 경험
- \(Z_4\): 직급, 재직기간, 직무유형
- \(Z_5\): 조직문화

이 변수들은 연민적 공감 역량에도 영향을 줄 수 있고, 동시에 행정부담을 얼마나 수용적으로 보는가에도 영향을 줄 수 있다.

<figure class="chapter-figure">
  <svg viewBox="0 0 860 340" role="img" aria-label="연민적 공감과 행정부담 태도의 확장 DAG">
    <rect x="360" y="60" width="150" height="60" rx="16" fill="#e8f2ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="435" y="87" text-anchor="middle" font-size="18" fill="#1e3a5f">X</text>
    <text x="435" y="108" text-anchor="middle" font-size="14" fill="#1e3a5f">연민적 공감</text>

    <rect x="620" y="60" width="170" height="60" rx="16" fill="#fff4e6" stroke="#d97706" stroke-width="2"/>
    <text x="705" y="87" text-anchor="middle" font-size="18" fill="#7c3d00">Y</text>
    <text x="705" y="108" text-anchor="middle" font-size="14" fill="#7c3d00">행정부담 관용 태도</text>

    <rect x="70" y="25" width="180" height="46" rx="14" fill="#eef2f7" stroke="#64748b"/>
    <text x="160" y="54" text-anchor="middle" font-size="14" fill="#334155">Z1 공공봉사동기</text>

    <rect x="70" y="90" width="180" height="46" rx="14" fill="#eef2f7" stroke="#64748b"/>
    <text x="160" y="119" text-anchor="middle" font-size="14" fill="#334155">Z2 이념·복지관·형평규범</text>

    <rect x="70" y="155" width="180" height="46" rx="14" fill="#eef2f7" stroke="#64748b"/>
    <text x="160" y="184" text-anchor="middle" font-size="14" fill="#334155">Z3 현장 민원 접촉 경험</text>

    <rect x="70" y="220" width="180" height="46" rx="14" fill="#eef2f7" stroke="#64748b"/>
    <text x="160" y="249" text-anchor="middle" font-size="14" fill="#334155">Z4 직급·재직기간·직무</text>

    <rect x="70" y="285" width="180" height="46" rx="14" fill="#eef2f7" stroke="#64748b"/>
    <text x="160" y="314" text-anchor="middle" font-size="14" fill="#334155">Z5 조직문화</text>

    <line x1="250" y1="48" x2="360" y2="86" stroke="#475569" stroke-width="2.5"/><polygon points="360,86 346,79 348,93" fill="#475569"/>
    <line x1="250" y1="48" x2="620" y2="86" stroke="#475569" stroke-width="2.5"/><polygon points="620,86 606,79 608,93" fill="#475569"/>

    <line x1="250" y1="113" x2="360" y2="92" stroke="#475569" stroke-width="2.5"/><polygon points="360,92 345,87 348,101" fill="#475569"/>
    <line x1="250" y1="113" x2="620" y2="92" stroke="#475569" stroke-width="2.5"/><polygon points="620,92 605,87 608,101" fill="#475569"/>

    <line x1="250" y1="178" x2="360" y2="98" stroke="#475569" stroke-width="2.5"/><polygon points="360,98 349,107 357,118" fill="#475569"/>
    <line x1="250" y1="178" x2="620" y2="98" stroke="#475569" stroke-width="2.5"/><polygon points="620,98 607,93 610,107" fill="#475569"/>

    <line x1="250" y1="243" x2="360" y2="104" stroke="#475569" stroke-width="2.5"/><polygon points="360,104 351,116 362,123" fill="#475569"/>
    <line x1="250" y1="243" x2="620" y2="104" stroke="#475569" stroke-width="2.5"/><polygon points="620,104 608,100 612,113" fill="#475569"/>

    <line x1="250" y1="308" x2="360" y2="110" stroke="#475569" stroke-width="2.5"/><polygon points="360,110 353,124 365,130" fill="#475569"/>
    <line x1="250" y1="308" x2="620" y2="110" stroke="#475569" stroke-width="2.5"/><polygon points="620,110 609,107 615,119" fill="#475569"/>

    <line x1="510" y1="90" x2="620" y2="90" stroke="#374151" stroke-width="3.2"/>
    <polygon points="620,90 605,82 605,98" fill="#374151"/>
  </svg>
  <figcaption>현실적인 DAG에서는 공공봉사동기, 이념, 직무특성, 조직문화 같은 공통원인이 X와 Y에 동시에 영향을 줄 수 있다.</figcaption>
</figure>

이 구조에서 핵심은 back-door 경로가 여러 개 존재한다는 점이다. 예를 들어

\[
X \leftarrow Z_1 \rightarrow Y,\qquad
X \leftarrow Z_2 \rightarrow Y
\]

같은 경로가 열려 있으면, 단순한 \(X\)와 \(Y\)의 상관은 인과효과와 교란이 뒤섞인 값이 된다. 따라서 총효과를 추정하려면 이런 공통원인을 조정하는 것이 기본 원칙이다.

## 매개변수(mediator)가 있을 때

이 가설은 심리적 경로를 통해 작동할 가능성이 크다. 예를 들면

- \(M_1\): 시민의 고통과 불편에 대한 인식
- \(M_2\): 행정부담의 불공정성 인식
- \(M_3\): 부담 완화 필요성 인식

같은 변수가 중간 경로를 형성할 수 있다.

<figure class="chapter-figure">
  <svg viewBox="0 0 920 200" role="img" aria-label="매개경로를 포함한 DAG">
    <rect x="40" y="70" width="150" height="58" rx="16" fill="#e8f2ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="115" y="96" text-anchor="middle" font-size="18" fill="#1e3a5f">X</text>
    <text x="115" y="116" text-anchor="middle" font-size="13" fill="#1e3a5f">연민적 공감</text>

    <rect x="245" y="70" width="140" height="58" rx="16" fill="#eef8ef" stroke="#2f855a" stroke-width="2"/>
    <text x="315" y="96" text-anchor="middle" font-size="18" fill="#21543a">M1</text>
    <text x="315" y="116" text-anchor="middle" font-size="13" fill="#21543a">시민 고통 인식</text>

    <rect x="435" y="70" width="140" height="58" rx="16" fill="#eef8ef" stroke="#2f855a" stroke-width="2"/>
    <text x="505" y="96" text-anchor="middle" font-size="18" fill="#21543a">M2</text>
    <text x="505" y="116" text-anchor="middle" font-size="13" fill="#21543a">불공정성 인식</text>

    <rect x="625" y="70" width="140" height="58" rx="16" fill="#eef8ef" stroke="#2f855a" stroke-width="2"/>
    <text x="695" y="96" text-anchor="middle" font-size="18" fill="#21543a">M3</text>
    <text x="695" y="116" text-anchor="middle" font-size="13" fill="#21543a">부담 완화 필요성</text>

    <rect x="790" y="70" width="110" height="58" rx="16" fill="#fff4e6" stroke="#d97706" stroke-width="2"/>
    <text x="845" y="96" text-anchor="middle" font-size="18" fill="#7c3d00">Y</text>
    <text x="845" y="116" text-anchor="middle" font-size="13" fill="#7c3d00">관용 태도</text>

    <line x1="190" y1="99" x2="245" y2="99" stroke="#374151" stroke-width="3"/><polygon points="245,99 231,91 231,107" fill="#374151"/>
    <line x1="385" y1="99" x2="435" y2="99" stroke="#374151" stroke-width="3"/><polygon points="435,99 421,91 421,107" fill="#374151"/>
    <line x1="575" y1="99" x2="625" y2="99" stroke="#374151" stroke-width="3"/><polygon points="625,99 611,91 611,107" fill="#374151"/>
    <line x1="765" y1="99" x2="790" y2="99" stroke="#374151" stroke-width="3"/><polygon points="790,99 776,91 776,107" fill="#374151"/>

    <path d="M 190 82 C 390 20, 650 20, 790 82" fill="none" stroke="#b45309" stroke-width="2.5" stroke-dasharray="8 6"/>
    <polygon points="790,82 776,75 778,89" fill="#b45309"/>
    <text x="510" y="40" text-anchor="middle" font-size="14" fill="#92400e">직접효과 경로</text>
  </svg>
  <figcaption>연민적 공감은 시민 고통 인식, 불공정성 인식, 부담 완화 필요성 인식을 거쳐 행정부담 관용 태도에 영향을 줄 수 있다.</figcaption>
</figure>

중요한 점은, 이런 변수들은 총효과를 추정할 때는 대개 **통제 대상이 아니라 설명 대상**이라는 것이다. 즉 매개경로를 알고 싶다면 유용하지만, 총효과를 알고 싶은 분석에서 \(M\)을 통제하면 오히려 \(X\)의 효과를 잘라내는 일이 된다.

## 충돌변수(collider)의 가능성

이 연구에서는 충돌변수를 잘못 통제할 위험도 꽤 크다. 충돌변수란 DAG에서 두 개 이상의 화살표가 한 변수로 모이는 경우다.

\[
X \rightarrow C \leftarrow U
\]

이때 \(C\)를 조건화하면 원래 막혀 있던 경로가 열려서 편의가 생길 수 있다.

### 예시 1. 감정노동 또는 정서적 소진

연민적 공감이 높은 공무원은 시민의 어려움에 더 민감하게 반응하므로 감정노동이나 소진을 더 크게 느낄 수 있다. 동시에 민원 강도, 악성 민원 노출 같은 미관측 요인 \(U\)도 소진을 높일 수 있다. 그리고 그 미관측 요인은 행정부담 관용 태도에도 영향을 줄 수 있다.

<figure class="chapter-figure">
  <svg viewBox="0 0 760 250" role="img" aria-label="충돌변수 사례 DAG">
    <rect x="60" y="95" width="150" height="58" rx="16" fill="#e8f2ff" stroke="#3b82f6" stroke-width="2"/>
    <text x="135" y="121" text-anchor="middle" font-size="18" fill="#1e3a5f">X</text>
    <text x="135" y="141" text-anchor="middle" font-size="13" fill="#1e3a5f">연민적 공감</text>

    <rect x="300" y="95" width="160" height="58" rx="16" fill="#fde8e8" stroke="#dc2626" stroke-width="2"/>
    <text x="380" y="121" text-anchor="middle" font-size="18" fill="#7f1d1d">C</text>
    <text x="380" y="141" text-anchor="middle" font-size="13" fill="#7f1d1d">감정노동·소진</text>

    <rect x="300" y="20" width="160" height="48" rx="14" fill="#f3f4f6" stroke="#6b7280" stroke-width="2" stroke-dasharray="6 4"/>
    <text x="380" y="49" text-anchor="middle" font-size="14" fill="#374151">U 민원강도·악성민원 노출</text>

    <rect x="550" y="95" width="160" height="58" rx="16" fill="#fff4e6" stroke="#d97706" stroke-width="2"/>
    <text x="630" y="121" text-anchor="middle" font-size="18" fill="#7c3d00">Y</text>
    <text x="630" y="141" text-anchor="middle" font-size="13" fill="#7c3d00">관용 태도</text>

    <line x1="210" y1="124" x2="300" y2="124" stroke="#374151" stroke-width="3"/><polygon points="300,124 286,116 286,132" fill="#374151"/>
    <line x1="380" y1="68" x2="380" y2="95" stroke="#374151" stroke-width="3"/><polygon points="380,95 372,81 388,81" fill="#374151"/>
    <line x1="460" y1="44" x2="550" y2="105" stroke="#374151" stroke-width="3"/><polygon points="550,105 536,100 541,113" fill="#374151"/>

    <path d="M 210 104 C 300 45, 460 45, 550 104" fill="none" stroke="#c2410c" stroke-width="2.5" stroke-dasharray="8 6"/>
    <text x="382" y="28" text-anchor="middle" font-size="13" fill="#c2410c">C를 통제하면 X → C ← U → Y 경로가 열릴 수 있음</text>
  </svg>
  <figcaption>감정노동이나 소진은 매개변수처럼 보이지만, 민원강도 같은 미관측 요인의 공동 결과라면 collider가 될 수 있다.</figcaption>
</figure>

이 구조에서 소진 \(C\)를 “통제해야 더 정확하겠지”라고 생각하고 회귀식에 넣으면,

\[
X \rightarrow C \leftarrow U \rightarrow Y
\]

경로가 열려 가짜 연관이 생길 수 있다.

### 예시 2. 시민접점 부서 배치 또는 선택적 교육훈련 참여

시민접점 부서 배치 결과나 시민중심 교육훈련 참여 여부도 조심해야 한다. 연민적 공감이 높은 공무원은 그런 부서나 교육을 더 선호할 수 있고, 동시에 상급자 판단이나 조직 수요도 같은 결과를 만들어 낼 수 있다. 이 경우 해당 변수는 공통원인이 아니라 collider일 수 있다.

## 무엇을 조정하고 무엇을 조정하지 말아야 하는가

이 사례를 바탕으로 총효과를 추정할 때의 원칙을 정리하면 다음과 같다.

### 조정 후보

- 공공봉사동기
- 복지관, 시민책임관, 형평성 규범, 이념
- 직무유형
- 재직기간
- 조직문화
- 선행적인 시민 접촉 경험

### 총효과 추정에서 신중해야 할 변수

- 시민의 고통 인식
- 불공정성 인식
- 부담 완화 필요성 인식

이 변수들은 대체로 매개변수일 가능성이 크다.

### 가급적 총효과 추정에서 제외할 변수

- 감정노동
- 정서적 소진
- 현재 민원 스트레스
- 시민접점 부서 배치 결과
- 선택된 교육훈련 참여 여부

이 변수들은 상황에 따라 collider가 될 수 있다.

## 정리

이 사례가 보여 주는 핵심은 간단하다. 같은 종류의 변수처럼 보여도 DAG에서 어디에 놓이느냐에 따라 역할이 완전히 달라진다.

- 공통원인(confounder)은 조정해야 하고
- 매개변수(mediator)는 총효과 추정에서 성급히 조정하면 안 되며
- 충돌변수(collider)는 통제하면 오히려 편의를 만들 수 있다.

따라서 DAG는 “그림을 예쁘게 그리는 도구”가 아니라, **실제로 어떤 변수를 회귀식에 넣고 빼야 하는지를 판단하는 설계 도구**다. 이런 점에서 사례 기반 DAG 분석은 편향 가능성을 사전에 점검하는 매우 실용적인 방법이 된다.
