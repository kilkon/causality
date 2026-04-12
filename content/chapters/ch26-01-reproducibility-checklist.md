---
title: 24장. 재현가능성 체크리스트
description: 정책평가 연구에서 재현가능성이 왜 중요한지, 무엇을 어떤 순서로 점검해야 하는지를 정리한다.
---

# 24장. 재현가능성 체크리스트

좋은 정책평가 연구는 새로운 추정치를 제시하는 것만으로 충분하지 않다. 연구 질문이 무엇이었는지, 어떤 식별 가정이 필요했는지, 자료를 어떻게 가공했는지, 어떤 사양을 기본 분석으로 채택했는지, 그리고 다른 연구자가 같은 자료와 코드로 같은 결과를 재현할 수 있는지가 함께 드러나야 한다. 재현가능성(reproducibility)은 결과를 보기 좋게 포장하는 마지막 단계가 아니라, 인과효과 추정의 신뢰성을 떠받치는 연구 절차 전체의 품질 관리 장치다.

정책평가에서는 이 문제가 특히 중요하다. 행정자료는 접근권한이 제한되어 있고, 여러 기관의 자료를 결합하는 과정이 길며, 식별전략도 종종 자료 정제 규칙, 시점 정의, 표본 제한, 민감도 분석에 크게 의존한다. 같은 회귀식이라도 누가 언제 어떤 규칙으로 분석 표본을 만들었는지에 따라 결론이 달라질 수 있다. 따라서 재현가능성은 단순히 코드를 공개했는가의 문제가 아니라, 연구의 논리와 절차가 제3자에게 검증 가능한 형태로 기록되었는가의 문제다.

## 24.0.1 왜 재현가능성이 정책평가에서 더 중요해지는가

정책평가 연구에서는 다음과 같은 이유로 재현가능성이 핵심 쟁점이 된다.

1. 정책효과 추정은 대개 여러 단계의 판단을 거친다. 표본 정의, 처리 변수 코딩, 제도 시행시점 정의, 결측 처리, 통제변수 선택, 민감도 분석 방식이 모두 결론에 영향을 준다.
2. 행정자료는 원자료(raw data)와 분석자료(analytic file) 사이 거리가 멀다. 이 과정이 문서화되지 않으면 동일한 추정치를 다시 만들기 어렵다.
3. 정책결정은 단일 추정치보다 그 추정치의 신뢰성과 재검증 가능성에 크게 의존한다. 같은 분석이 다른 시점이나 다른 연구자에게 반복될 수 있어야 정책 설계에 활용할 수 있다.
4. 최근의 인과 ML, 고차원 보정, 시뮬레이션 기반 분석은 계산 절차가 복잡해져 “결과는 화려하지만 재현은 어려운” 연구를 쉽게 만든다.

이를 식으로 요약하면, 재현가능성은 단순한 코드 공개가 아니라 다음 다섯 요소의 결합이다.

\[
\text{Reproducibility}
=
f(
\text{Question},
\text{Identification},
\text{Data Pipeline},
\text{Estimation},
\text{Sensitivity and Reporting})
\]

즉 재현가능성은 연구 질문, 식별 논리, 자료 생성과 가공 절차, 추정 코드, 민감도 점검과 보고 관행이 서로 일관되게 연결되어 있을 때 성립한다.

<figure class="figure">
  <svg viewBox="0 0 980 240" role="img" aria-label="재현가능성의 다섯 요소">
    <rect x="24" y="84" width="150" height="64" rx="14" fill="#dbeafe" stroke="#2563eb"/>
    <rect x="206" y="84" width="150" height="64" rx="14" fill="#dcfce7" stroke="#16a34a"/>
    <rect x="388" y="84" width="150" height="64" rx="14" fill="#fef3c7" stroke="#d97706"/>
    <rect x="570" y="84" width="150" height="64" rx="14" fill="#fae8ff" stroke="#a21caf"/>
    <rect x="752" y="84" width="190" height="64" rx="14" fill="#fee2e2" stroke="#dc2626"/>
    <text x="99" y="110" text-anchor="middle" font-size="18" fill="#1d4ed8">연구 질문</text>
    <text x="99" y="132" text-anchor="middle" font-size="14" fill="#1d4ed8">무엇을 추정하는가</text>
    <text x="281" y="110" text-anchor="middle" font-size="18" fill="#166534">식별 논리</text>
    <text x="281" y="132" text-anchor="middle" font-size="14" fill="#166534">왜 인과로 읽는가</text>
    <text x="463" y="110" text-anchor="middle" font-size="18" fill="#92400e">자료 파이프라인</text>
    <text x="463" y="132" text-anchor="middle" font-size="14" fill="#92400e">어떻게 분석표본이 되었는가</text>
    <text x="645" y="110" text-anchor="middle" font-size="18" fill="#86198f">추정 절차</text>
    <text x="645" y="132" text-anchor="middle" font-size="14" fill="#86198f">코드와 사양은 무엇인가</text>
    <text x="847" y="110" text-anchor="middle" font-size="18" fill="#991b1b">민감도와 보고</text>
    <text x="847" y="132" text-anchor="middle" font-size="14" fill="#991b1b">얼마나 견고한가</text>
    <line x1="174" y1="116" x2="206" y2="116" stroke="#64748b" stroke-width="3"/>
    <line x1="356" y1="116" x2="388" y2="116" stroke="#64748b" stroke-width="3"/>
    <line x1="538" y1="116" x2="570" y2="116" stroke="#64748b" stroke-width="3"/>
    <line x1="720" y1="116" x2="752" y2="116" stroke="#64748b" stroke-width="3"/>
  </svg>
  <figcaption>재현가능성은 결과표 하나의 문제가 아니라 질문, 식별, 자료 가공, 추정, 민감도 보고가 모두 연결된 연구 체계의 문제다.</figcaption>
</figure>

## 24.0.2 재현가능성은 왜 식별 검토와 직결되는가

정책평가에서 재현가능성은 단순한 계산의 반복 가능성보다 더 넓은 의미를 갖는다. 인과효과 연구에서는 “같은 코드로 같은 숫자가 다시 나온다”는 사실만으로 충분하지 않다. 그 숫자가 어떤 인과량을 의미하는지, 어떤 식별 가정 아래 해석되는지, 그 가정이 자료 처리와 모형 선택 속에 어떻게 구현되었는지가 분명해야 한다.

예를 들어 다음 세 연구를 생각해 보자.

1. 회귀모형으로 프로그램 참여 효과를 추정했지만, 어떤 통제변수가 사전변수이고 어떤 변수가 처치 이후 변수인지 구분이 없다.
2. DID를 사용했지만 정책 시행시점 코딩 규칙이 코드 주석에도 논문에도 명시되지 않았다.
3. 성향점수 가중치를 썼지만 trimming 규칙, overlap 점검, 극단 가중치 처리 방식이 공개되지 않았다.

이 경우 계산 자체는 반복할 수 있어도 식별 논리는 검증할 수 없다. 재현가능성의 핵심은 숫자를 복제하는 것이 아니라, 숫자에 이르는 식별 논리와 분석 절차를 재구성할 수 있게 만드는 데 있다.

## 24.0.3 정책평가 연구자가 실제로 점검해야 할 순서

재현가능성 점검은 보통 다음 순서로 진행하는 것이 좋다.

1. 연구 질문과 estimand를 문장과 수식으로 분명히 쓴다.
2. 식별 전략과 필요한 가정을 명시한다.
3. 원자료에서 분석자료가 만들어지는 전처리 과정을 재실행 가능하게 남긴다.
4. 기본 사양(main specification)과 대안 사양(alternative specifications)을 구분한다.
5. 민감도 분석, placebo, robustness check를 별도 섹션에서 보고한다.
6. 제3자가 다시 실행할 수 있는 코드·문서·로그를 남긴다.

이 절차를 보다 형식적으로 쓰면 다음과 같다.

\[
\text{Raw data}
\rightarrow
\text{analytic sample}
\rightarrow
\text{identified estimand}
\rightarrow
\text{implemented estimator}
\rightarrow
\text{robustness and interpretation}
\]

좋은 재현가능성 보고는 이 다섯 단계를 모두 문서화한다.

## 24.0.4 행정자료와 정책자료에서 특히 강조해야 할 항목

정책평가에서는 다음 항목을 별도로 점검해야 한다.

### 자료 접근과 가공 기록

행정자료는 종종 원자료를 직접 공개할 수 없다. 이 경우에도 분석 표본이 어떻게 구성되었는지, 어떤 기준으로 자료를 병합했고 어떤 익명화 규칙을 적용했는지, 누락치와 중복을 어떻게 처리했는지 문서화해야 한다.

### 처리와 결과의 운영적 정의

같은 정책이라도 “수급 자격을 얻은 것”과 “실제로 서비스를 이용한 것”과 “일정 기간 이상 참여한 것”은 모두 다른 처치 정의다. 결과변수 역시 단기 산출, 중기 성과, 장기 사회적 효과를 구분해야 한다. 재현가능성은 이런 정의가 코드와 문서에서 일치할 때 확보된다.

### 설계 단계와 분석 단계의 구분

실험, IV, RDD, DID, 매칭, 가중치 등 어떤 설계를 쓰든, 식별의 핵심은 설계 단계에서 정해지고 추정은 그 다음이다. 따라서 논문에는 “왜 이 설계가 비교가능성을 보장하는가”가 먼저 나오고, “어떻게 계산했는가”가 뒤따라야 한다.

### 민감도 분석과 해석 범위

재현가능성은 기본 회귀표를 다시 만드는 데서 끝나지 않는다. 동일한 자료로 trimming 규칙을 바꾸었을 때, bandwidth를 줄였을 때, placebo 시점을 썼을 때, 다른 함수형을 적용했을 때 결론이 얼마나 유지되는지도 함께 보고해야 한다.

## 24.0.5 24장의 구조

이 장은 재현가능성 점검을 네 개의 실천 항목으로 나누어 살펴본다.

1. [24.1 연구 질문·식별 가정·추정 절차의 일관성 점검](/C:/Users/owner/causal%20inference/causal%20inference2/content/chapters/ch26-02-s261.md)
2. [24.2 사전분석계획(pre-analysis plan)과 분석 자유도 관리](/C:/Users/owner/causal%20inference/causal%20inference2/content/chapters/ch26-03-s262.md)
3. [24.3 재현 가능 보고 표준: 코드·데이터·민감도 공개](/C:/Users/owner/causal%20inference/causal%20inference2/content/chapters/ch26-04-s263.md)
4. [24.4 정책 해석에서 내부·외부 타당도의 분리 보고](/C:/Users/owner/causal%20inference/causal%20inference2/content/chapters/ch26-05-s264.md)

이 장의 목표는 단지 “재현이 중요하다”는 선언을 반복하는 것이 아니다. 정책평가 연구자가 실제로 어떤 자료, 어떤 문서, 어떤 코드, 어떤 점검 절차를 갖추어야 하는지 구체적으로 제시하는 데 있다.
