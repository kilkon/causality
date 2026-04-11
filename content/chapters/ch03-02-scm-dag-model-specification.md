---
title: 3.2 식별의 다양한 의미 - Lewbel의 Identification Zoo
description: 식별이 단 하나의 개념처럼 보이지만 실제 계량경제학과 인과추론에서는 여러 층위와 변형이 존재한다는 점을 Lewbel의 정리로 설명한다.
---

# 3.2 식별의 다양한 의미 - Lewbel의 Identification Zoo
3.1절에서 우리는 모형 설정, 식별, 추정을 구분해야 한다고 보았다. 그런데 막상 식별이라는 단어를 조금 더 깊이 들여다보면, 문헌에서는 이 말을 매우 다양한 방식으로 사용한다. 어떤 논문은 점 식별(point identification)을 말하고, 어떤 논문은 부분 식별(partial identification)을 말하며, 또 어떤 논문은 지역 식별(local identification), 약한 식별(weak identification), 식별 at infinity, causal identification, structural identification 같은 표현을 쓴다.

Arthur Lewbel의 2019년 논문 *The Identification Zoo*는 바로 이 혼란을 정리한 글이다. Lewbel의 핵심 메시지는 단순하다. 식별은 본래 "관찰 가능한 모집단 분포로부터 관심 모수나 관심 특성이 유일하게 결정되는가"라는 하나의 핵심 뜻을 갖지만, 실제 계량경제학과 인과추론 문헌에서는 이 하나의 뜻이 여러 변형된 형태로 사용되어 왔다는 것이다. 이 절은 그 지도를 소개한다.

## 3.2.1 Lewbel이 말하는 식별의 출발점

Lewbel은 계량경제학에서 식별이 궁극적으로 의미하는 바를 다음처럼 정리한다. 관심 모수 또는 관심 대상이 관찰 가능한 모집단(population of observables)으로부터 유일하게 결정되면 식별되었다고 말한다. 직관적으로 쓰면

\[
\theta \text{ is identified } \Longleftrightarrow \theta = g(P(O))
\]

인 어떤 함수 \(g\)가 존재하는 경우이다. 여기서 \(O\)는 관찰가능한 자료, \(P(O)\)는 그 모집단 분포, \(\theta\)는 알고 싶은 모수 또는 함수형(functional)이다.

이 정의가 중요한 이유는 식별을 표본추정이나 통계적 유의성과 구분해 주기 때문이다. 식별은 유한표본에서 계산이 잘 되는가를 묻는 것이 아니라, 설령 무한히 많은 데이터를 갖고 있어도 관찰 가능한 정보만으로 관심량을 복원할 수 있는가를 묻는 것이다.

즉 Lewbel은 3.1절의 핵심을 더 정교한 언어로 다시 말한다. 식별은 추정 이전의 문제이다.

## 3.2.2 왜 'Zoo'인가

Lewbel이 굳이 "동물원(zoo)"이라는 표현을 쓴 이유는, 식별 관련 용어가 너무 많고 서로 겹치기 때문이다. 논문 초반부에서 그는 문헌에 등장하는 수십 개의 용어를 나열한다. 예를 들어

- point identification
- set identification
- local identification
- generic identification
- weak identification
- irregular identification
- identification at infinity
- structural identification
- causal identification
- nonparametric identification
- semiparametric identification
- overidentification

같은 표현들이 함께 등장한다.

Lewbel의 문제의식은 "식별이라는 말이 너무 많이 쓰인다"가 아니다. 오히려 각각이 어떤 상황에서 쓰이고, 어떤 층위의 차이를 가리키는지 구분하지 않으면 연구자들끼리 전혀 다른 문제를 놓고 같은 단어를 쓰게 된다는 데 있다.

## 3.2.3 점 식별(point identification)이 기본 개념이다

Lewbel은 가장 기본적인 개념으로 점 식별(point identification)을 둔다. 점 식별이란 관심량이 하나의 값으로 유일하게 결정된다는 뜻이다.

\[
\theta = g(P(O))
\]

가 정확히 하나의 값을 주면 점 식별이다.

예를 들어 무작위배정된 실험에서 평균처치효과가

\[
\mathrm{ATE}
=
\mathbb{E}[Y\mid D=1]-\mathbb{E}[Y\mid D=0]
\]

로 표현되면, 주어진 모집단 분포에서 ATE는 점 식별된 것이다.

Lewbel의 관점에서 이 정의는 식별의 출발점이자 기준점이다. 다른 많은 개념은 사실 점 식별이 실패하거나 약화되거나 제한된 경우를 이름 붙인 것에 가깝다.

## 3.2.4 부분 식별(set identification)과 식별 실패

모든 연구가 점 식별을 달성하는 것은 아니다. 때로는 데이터와 가정만으로 관심량을 하나의 점으로 결정할 수 없고, 가능한 값의 집합만 얻는다. 이것이 부분 식별 또는 집합 식별(set identification)이다.

\[
\theta \in \Theta(P(O))
\]

처럼 가능한 값들의 집합 \(\Theta(P(O))\)만 알 수 있다면, 이는 점 식별이 아니라 부분 식별이다.

이 개념은 매우 중요하다. 왜냐하면 많은 연구가 실제로는 점 식별을 달성하지 못하면서도, 결과를 마치 하나의 정확한 숫자인 것처럼 보고하기 쉽기 때문이다. Lewbel은 이런 구분을 명확히 해야 한다고 강조한다.

이 점은 Manski의 부분 식별 전통과도 자연스럽게 이어진다. 즉 식별이 안 되는 상황에서 억지로 점추정을 하기보다, 어떤 가정 아래 가능한 값의 범위를 보고하는 것이 더 정직할 수 있다.

## 3.2.5 지역 식별(local identification)과 전역 식별(global identification)

어떤 모형에서는 특정 모수 근방에서만 유일성이 성립할 수 있다. 이것이 지역 식별(local identification)이다. 반면 모수공간 전체에서 유일성이 성립하면 전역 식별(global identification)이라고 부른다.

직관적으로 말하면, 지역 식별은 "참값 근처에서는 다른 모수값과 구별된다"는 뜻이고, 전역 식별은 "모수공간 어디에서도 같은 관찰분포를 만드는 다른 값이 없다"는 뜻이다.

이 구분은 구조모형에서 특히 중요하다. 비선형 모형이나 동시방정식 모형에서는 국소적으로는 식별되지만, 멀리 떨어진 다른 모수값이 같은 관찰분포를 만들 수도 있다. 이 경우 추정 알고리즘은 하나의 해를 찾더라도, 이론적으로는 완전한 전역 식별이 아닐 수 있다.

## 3.2.6 generic identification의 의미

generic identification은 모든 모수값에서 식별이 성립하는 것은 아니지만, "예외적인 특수한 경우를 제외하면" 대부분의 모수값에서 식별된다는 뜻이다. 즉 식별 실패가 measure zero에 가까운 특수한 경우에만 발생한다는 생각이다.

이 개념은 선형구조모형이나 네트워크모형처럼 특정 매개변수 조합에서만 퇴화(degenerate) 현상이 생기는 경우에 유용하다. 실무적으로는 "거의 항상 식별된다"고 말할 수 있지만, 이론적으로는 완전한 전역 식별과는 다르다.

Lewbel은 이런 표현이 실제로는 매우 다른 강도의 주장을 담고 있으므로, generic이라는 말을 쓸 때 그 예외집합이 무엇인지 분명히 해야 한다고 본다.

## 3.2.7 weak identification은 무엇이 다른가

weak identification은 점 식별 여부와 추론의 안정성이 만나는 지점에 있다. 관심 모수가 이론적으로는 식별될 수 있어도, 데이터가 그 모수를 충분히 강하게 구별하지 못하면 weak identification 문제가 생긴다.

가장 대표적인 예는 도구변수 모형에서 약한 도구변수(weak instruments)이다. 예를 들어 2SLS에서 도구 \(Z\)가 처치 \(D\)를 거의 설명하지 못하면, 이론상 식별은 되어도 실제 추정량의 분산이 커지고 정규근사도 불안정해진다.

따라서 weak identification은 단순히 "식별이 없다"는 뜻이 아니라, "식별의 정보가 너무 약해서 표준적 추론이 위험해진다"는 뜻이다. 이 개념은 3.1절에서 말한 식별과 추정가능성의 차이를 잘 보여 준다.

## 3.2.8 identification at infinity와 기능형태에 의한 식별

Lewbel은 identification at infinity, 그리고 기능형태(functional form)에 의한 식별도 중요한 범주로 다룬다. 어떤 모형에서는 공변량이나 도구변수가 극단적 값을 가질 때만 특정 효과가 드러나기도 한다. 예를 들어 selection model이나 treatment model에서 support의 꼬리 부분에서만 반사실 비교가 가능해지는 경우가 있다.

이런 식별은 이론적으로는 가능하지만, 실무적으로는 데이터의 희소성 때문에 매우 불안정할 수 있다. 따라서 "식별된다"는 말만으로 충분하지 않고, 어디에서, 어떤 정보에 기대어 식별되는지도 함께 말해야 한다.

또한 Lewbel은 고차 모멘트(second and higher moments)나 이분산성을 이용해 "구성된 도구변수(constructed instruments)"를 만들 수 있다는 자신의 연구 전통과도 연결한다. 이 역시 기능형태와 오차구조에 강하게 기대는 식별의 한 예이다.

## 3.2.9 구조모형의 식별과 causal/reduced-form 식별은 어떻게 다른가

Lewbel 논문에서 매우 중요한 부분은 전통적 구조모형(structural models)과 causal/reduced-form 문헌의 식별을 비교하는 대목이다.

전통적 구조모형에서는

- 구조방정식
- 배제 제약
- 차수조건과 계수조건
- reduced form의 존재

같은 개념이 핵심이다. 여기서는 "구조계수(structural parameters)가 관찰가능한 reduced-form 분포로부터 복원되는가"가 중심 질문이다.

반면 causal inference 또는 treatment-effects 문헌에서는

- 잠재결과
- 무작위배정
- 조건부 독립성
- 도구변수 가정
- RDD 연속성
- DID 평행추세

같은 가정이 중심이다. 여기서는 "특정 인과효과가 관찰분포로부터 복원되는가"가 중심 질문이다.

Lewbel의 중요한 메시지는, 이 둘이 완전히 다른 문제는 아니라는 점이다. 둘 다 결국 관찰가능한 모집단 분포로부터 관심량이 유일하게 결정되는가를 묻는다. 다만 구조모형 문헌은 방정식과 모수의 언어를, causal 문헌은 잠재결과와 설계의 언어를 더 많이 사용해 왔다.

이 점은 이 책의 전체 방향과도 잘 맞는다. 우리는 3.1절에서 세 층위를 구분했고, 이후 장들에서는 설계 기반 식별 전략을 더 많이 보겠지만, Lewbel은 이 모든 것이 넓게 보면 같은 식별 문제의 다른 표현임을 상기시킨다.

## 3.2.10 normalization, coherence, completeness

Lewbel은 식별과 가까운 개념들로 normalization, coherence, completeness도 함께 논의한다.

### normalization

정규화(normalization)는 모형의 본질적 내용을 바꾸지 않으면서 스케일이나 방향을 고정하는 제약이다. 예를 들어 잠재지수모형에서 분산을 1로 두는 것은 정규화일 수 있다. 이런 제약은 계산과 해석을 위해 필요하지만, 진짜 식별과 혼동하면 안 된다.

즉 어떤 제약은 "모형을 하나로 대표하도록 표준화"하는 것이고, 어떤 제약은 "관찰자료로부터 유일성 자체를 확보"하는 것이다. Lewbel은 이 둘을 분명히 나누어야 한다고 강조한다.

### coherence

coherence는 대체로 모형이 서로 양립 가능한 구조를 갖는가, 즉 모순 없는 방식으로 정의되는가의 문제와 연결된다. 특히 reduced form의 존재 가능성과 관련해 논의된다.

### completeness

completeness는 모형이 관찰자료의 분포를 충분히 규정하고 있는가, 혹은 어떤 부분이 비워져 있어 여러 observationally equivalent structures가 남는가와 관련된다. 불완전한 모형은 애초에 식별 논의를 어렵게 만든다.

이 개념들은 본문에서 자주 직접 등장하지는 않더라도, 왜 어떤 모형은 식별 이전에 먼저 "모형 자체가 충분히 닫혀 있는가"를 물어야 하는지 이해하게 해 준다.

## 3.2.11 식별은 가설의 강도를 드러내는 언어이기도 하다

Lewbel 논문의 장점은 식별을 단순한 기술용어가 아니라 가정의 강도를 보여주는 언어로 읽게 해 준다는 점이다. 예를 들어

- point identified라고 말하면 강한 유일성 주장을 하는 것이고
- set identified라고 말하면 유일성을 포기하고 집합으로 말하는 것이며
- weakly identified라고 말하면 유일성은 있어도 정보가 약하다고 말하는 것이고
- local identified라고 말하면 전역이 아니라 근방의 유일성만 주장하는 것이다.

즉 식별 용어는 결과를 포장하는 장식어가 아니라, 연구자가 무엇을 얼마나 강하게 주장하는지를 드러내는 메타언어이다.

## 3.2.12 이 책을 읽을 때 Lewbel의 분류를 어떻게 활용할 것인가

이 책의 이후 장들을 읽을 때 Lewbel의 분류는 다음처럼 도움이 된다.

- RCT는 보통 특정 효과의 점 식별을 제공한다.
- 관측연구의 회귀조정과 매칭은 조건부 독립성 아래의 점 식별 주장이다.
- IV는 특정 하위집단 효과의 점 식별 또는 국소 식별 논리로 읽을 수 있다.
- 부분 식별과 민감도 분석 장에서는 점 식별을 포기한 경우를 다룬다.
- weak IV, weak overlap, irregular problems는 식별과 추론이 함께 흔들리는 경우이다.

즉 Lewbel의 identification zoo는 단순한 용어 정리가 아니라, 이후 장들에서 각 방법이 실제로 어떤 종류의 식별 주장을 하고 있는지를 읽는 지도 역할을 한다.

## 3.2.13 이 절의 정리

핵심을 요약하면 다음과 같다.

- Lewbel은 식별의 기본 뜻을 "관찰 가능한 모집단 분포로부터 관심량이 유일하게 결정되는가"로 정리한다.
- 점 식별은 기본 개념이고, 부분 식별, 지역 식별, generic identification, weak identification 등은 그 변형된 형태이다.
- 구조모형 문헌과 causal/reduced-form 문헌은 언어는 다르지만, 결국 같은 식별 문제를 다룬다.
- normalization, coherence, completeness는 식별과 밀접하지만 동일한 개념은 아니다.
- 식별 용어는 연구자가 어떤 강도의 주장을 하는지를 드러내는 언어이다.

다음 절에서는 이런 식별 개념을 바탕으로, 관찰자료의 분포에서 인과적 대상까지 어떻게 건너가는지를 더 직접적으로 살펴본다.
