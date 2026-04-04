---
title: 1.1 상관과 인과의 근본적 차이 — 왜 회귀만으로는 부족한가
description: 
---

# 1.1 상관과 인과의 근본적 차이 — 왜 회귀만으로는 부족한가

## 1.1.1 데이터는 언제나 상관만 말한다
    통계학을 처음 배우는 학생은 대부분 같은 충고를 듣는다.

    > 「상관관계는 인과관계가 아니다 (*correlation does not imply causation*).」

      그런데 이 문장은 너무 자주 반복된 나머지 그 의미가 닳아 없어진 것처럼 느껴진다. 사람들은 이 경고를 들으면 고개를 끄덕이고, 그다음 줄에서 곧바로 회귀계수를 「A가 B에 미치는 효과」라고 해석한다. 이 책은 그 간극을 메우기 위해 쓰였다.

      문제의 핵심은 **데이터 자체가 근본적으로 상관(association)의 언어로만 말한다**는 점이다. 우리가 관측하는 데이터는 어떤 변수가 어떤 값을 취했을 때 다른 변수가 어떤 값을 취했는지에 대한 기록이다. 다시 말해, 데이터는 세계가 실제로 어떻게 전개되었는가(**factual**)를 담고 있을 뿐, 만약 세계가 달랐다면 어떻게 전개되었을까(**counterfactual**)에 대해서는 침묵한다. 인과 질문은 본질적으로 이 두 번째 물음, 즉 반사실의 언어로 표현된다. 그렇다면 상관으로부터 인과를 끌어내려는 시도는 왜 실패하는가? 이 절에서는 그 이유를 구체적으로 살펴본다.

    ## 1.1.2 직관적 예시: 신발을 신고 자면 두통이 생기는가

      고전적인 예시에서 시작하자. 어떤 도시의 응급실 데이터를 분석했더니, 신발을 신은 채로 잠든 사람들이 그렇지 않은 사람들보다 다음 날 아침 두통을 호소하는 비율이 유의미하게 높았다고 하자. 회귀분석을 돌리면 「신발을 신고 자는 것(*X*)이 두통(*Y*)과 양(+)의 상관을 가진다」는 결과가 나온다. 그렇다면 신발을 벗고 자면 두통이 줄어들까?

      물론 그렇지 않다. 신발을 신고 자는 행동과 두통은 둘 다 전날 밤 음주(*Z*)라는 **공통 원인(common cause)**에서 비롯된다. 음주를 많이 한 사람은 신발을 벗을 여유 없이 잠들고, 또한 다음 날 두통에 시달린다. 신발과 두통 사이의 상관은 실재하지만, 인과는 없다. 이처럼 두 변수가 공통 원인을 공유할 때 발생하는 허위 상관을 **교란(confounding)**이라 부른다.

      이 예시가 단순해 보이는 이유는 우리가 *Z*(음주)를 쉽게 떠올릴 수 있기 때문이다. 진짜 문제는 교란 변수가 측정되지 않았거나, 그것이 교란 변수인지조차 모르는 상황이다. 데이터는 *X*와 *Y*의 공동 분포를 알려줄 뿐, 그 분포가 어떤 구조에서 생성되었는지는 알려주지 않는다.

<svg width="440" height="168" viewBox="0 0 440 168" xmlns="http://www.w3.org/2000/svg" font-family="Pretendard, 'Malgun Gothic', sans-serif">
        <defs>
          <marker id="fig1-arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto" markerUnits="strokeWidth">
            <polygon points="0 0, 9 4.5, 0 9" fill="#37474f"/>
          </marker>
        </defs>
        <!-- 제목 (SVG 내부에는 HTML em 사용 불가 — tspan만 사용) -->
        <text x="220" y="20" text-anchor="middle" font-size="12" fill="#1e4d6b" font-weight="700">
          <tspan>그림 1. 음주(</tspan><tspan font-style="italic">Z</tspan><tspan>)가 신발(</tspan><tspan font-style="italic">X</tspan><tspan>)과 두통(</tspan><tspan font-style="italic">Y</tspan><tspan>)의 공통 원인</tspan>
        </text>
        <!-- Z: 교란 -->
        <circle cx="220" cy="68" r="28" fill="#fff3e0" stroke="#e65100" stroke-width="2"/>
        <text x="220" y="64" text-anchor="middle" font-size="11" font-weight="700" fill="#333">
          <tspan font-style="italic">Z</tspan>
        </text>
        <text x="220" y="78" text-anchor="middle" font-size="10" fill="#333">음주</text>
        <text x="220" y="92" text-anchor="middle" font-size="9" fill="#555">(교란)</text>
        <!-- X, Y -->
        <circle cx="95" cy="118" r="26" fill="#e8f5ef" stroke="#1d6b4a" stroke-width="2"/>
        <text x="95" y="114" text-anchor="middle" font-size="11" font-weight="600" fill="#333">
          <tspan font-style="italic">X</tspan>
        </text>
        <text x="95" y="128" text-anchor="middle" font-size="9.5" fill="#333">신발</text>
        <circle cx="345" cy="118" r="26" fill="#fce4ec" stroke="#8b2942" stroke-width="2"/>
        <text x="345" y="114" text-anchor="middle" font-size="11" font-weight="600" fill="#333">
          <tspan font-style="italic">Y</tspan>
        </text>
        <text x="345" y="128" text-anchor="middle" font-size="9.5" fill="#333">두통</text>
        <!-- Z 하단에서 X, Y 원의 상단 가장자리로 향하는 화살표 -->
        <line x1="205" y1="92" x2="115" y2="100" stroke="#37474f" stroke-width="2" marker-end="url(#fig1-arrow)"/>
        <line x1="235" y1="92" x2="325" y2="100" stroke="#37474f" stroke-width="2" marker-end="url(#fig1-arrow)"/>
        <!-- X-Y 직접 경로 없음(점선) -->
        <line x1="121" y1="118" x2="319" y2="118" stroke="#90a4ae" stroke-width="1.5" stroke-dasharray="6 5"/>
        <text x="220" y="114" text-anchor="middle" font-size="8.5" fill="#78909c">직접 인과 경로 없음</text>
        <!-- 하단 설명 -->
        <text x="220" y="156" text-anchor="middle" font-size="9.5" fill="#546e7a">
          <tspan font-style="italic">X</tspan><tspan>와 </tspan><tspan font-style="italic">Y</tspan><tspan> 사이에 화살표가 없어도 </tspan><tspan font-style="italic">Z</tspan><tspan>를 통한 연관으로 상관은 관측될 수 있음</tspan>
        </text>
      </svg>

      **그림 1.** 공통 원인 구조 *X* ← *Z* → *Y*. *X*와 *Y* 사이에 직접 인과 경로가 없어도 *Z*를 통한 연관이 생긴다.

:::

## 1.1.3 회귀는 무엇을 추정하는가

회귀분석은 변수들 사이의 조건부 연관을 요약하는 통계 도구다. 그래서 회귀계수는 매우 유용하지만, 그 자체로 곧바로 인과효과를 뜻하지는 않는다.

가장 익숙한 선형회귀식을 보자.

\[
Y_i = \alpha + \beta X_i + \gamma Z_i + \varepsilon_i
\]

이 식에서 많은 사람이 \(\hat{\beta}\)를 자동으로 “\(X\)의 효과”라고 읽는다. 하지만 실제로 회귀가 추정하는 것은 더 조심스럽게 이해해야 한다.

\[
\operatorname{plim}\hat{\beta}
=
\frac{\operatorname{Cov}(X, Y \mid Z)}{\operatorname{Var}(X \mid Z)}
\]

즉 \(Z\)를 조건으로 두었을 때 \(X\)와 \(Y\)가 얼마나 함께 움직이는지를 \(X\)의 조건부 분산으로 나눈 값이다. 이것은 **조건부 연관의 요약치**이지, 자동으로 인과효과의 크기를 뜻하는 것은 아니다. 다시 말해 회귀는 기본적으로 “\(X\)가 1단위 변할 때 \(Y\)가 평균적으로 얼마나 달라지는가”를 관측 데이터 안에서 요약할 뿐, 그 변화가 정말로 인과적 개입의 결과인지는 별도의 가정에 달려 있다.

회귀계수를 인과적으로 읽으려면 적어도 \(Z\)를 통제한 뒤 \(X\)와 \(Y\) 사이에 남아 있는 연관이 교란되지 않았다고 볼 수 있어야 한다. 이것이 흔히 **조건부 독립 가정**(conditional independence assumption), 혹은 **무시 가능성**(ignorability)이라고 불리는 생각이다. 이 가정은 데이터가 스스로 증명해 주는 것이 아니라, 연구 설계와 도메인 지식, 그리고 자료 생성 과정에 대한 이해를 통해 정당화되어야 한다.

**즉 회귀는 인과효과를 직접 보여주는 기계가 아니다. 회귀는 인과 가정이 주어졌을 때 그 가정을 수치로 번역하는 도구다.**

## 1.1.4 세 가지 구체적 실패 유형
    회귀가 인과 추론에 실패하는 상황을 세 가지 유형으로 분류할 수 있다.

    **① 교란(Confounding): 공통 원인에 의한 허위 상관**

      가장 널리 알려진 경우다. *X* ← *Z* → *Y* 구조에서, *Z*를 통제하지 않으면 *X* → *Y*의 상관이 나타나지만 이는 인과가 아니다. 아이스크림 판매량과 익사 사고 건수는 모두 날씨(기온)라는 공통 원인을 가진다. 아이스크림이 익사를 유발하지는 않는다. 중요한 것은, *Z*를 관측하지 못했다면(**unobserved confounding**) 회귀에 포함시킬 수가 없고, 그 경우 *β̂*은 편향된다.

    **② 역인과(Reverse Causation): 방향의 혼동**

      데이터는 변수 간의 방향을 알려주지 않는다. 경찰관 수(*X*)와 범죄율(*Y*) 사이의 양(+)의 상관을 보고 「경찰관이 많을수록 범죄가 늘어난다」고 결론 내릴 수 있을까? 실제로는 범죄율이 높은 지역에 경찰을 더 많이 배치하기 때문에(*Y* → *X*) 이 상관이 나타난다. 인과의 방향이 반대인 것이다. 회귀계수 *β̂*의 추정값과 통계적 유의성은 인과의 방향에 대해 아무것도 알려주지 않는다.

    **③ 콜라이더 편향(Collider Bias): 통제함으로써 생기는 편향**

      아마도 가장 반직관적인 실패 유형이다. *X* → *Z* ← *Y* 구조에서, *Z*는 *X*와 *Y* 모두의 결과(collider)다. 이 경우 *X*와 *Y*는 원래 독립이지만, *Z*를 통제(조건화)하면 *X*와 *Y* 사이에 허위 상관이 생긴다. 직관적 예로, 재능(*X*)과 노력(*Y*)이 독립적이더라도 「성공한 사람들(*Z*)」만을 표본으로 하면 재능과 노력이 음(−)의 상관을 보이는 것처럼 보일 수 있다. 더 많은 노력 없이도 성공한 사람은 재능이 뛰어날 가능성이 높기 때문이다. 교과서적 회귀 분석에서 「관련 변수는 모두 통제하라」는 조언은 콜라이더를 통제하면 오히려 편향을 만들어낸다는 사실을 무시한다.

<svg width="480" height="130" viewBox="0 0 480 130" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <marker id="m2" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#333"/></marker>
        </defs>
        <text x="80" y="18" text-anchor="middle" font-size="10" font-weight="700" fill="#1e4d6b">① 교란</text>
        <circle cx="80" cy="55" r="16" fill="#e8f0f5" stroke="#1e4d6b"/><text x="80" y="59" text-anchor="middle" font-size="9">Z</text>
        <circle cx="35" cy="95" r="14" fill="#fff" stroke="#555"/><text x="35" y="98" text-anchor="middle" font-size="9">X</text>
        <circle cx="125" cy="95" r="14" fill="#fff" stroke="#555"/><text x="125" y="98" text-anchor="middle" font-size="9">Y</text>
        <line x1="70" y1="68" x2="45" y2="85" stroke="#333" marker-end="url(#m2)"/>
        <line x1="90" y1="68" x2="115" y2="85" stroke="#333" marker-end="url(#m2)"/>
        <text x="240" y="18" text-anchor="middle" font-size="10" font-weight="700" fill="#1e4d6b">② 역인과</text>
        <circle cx="240" cy="55" r="14" fill="#fff" stroke="#555"/><text x="240" y="59" text-anchor="middle" font-size="9">Y</text>
        <circle cx="240" cy="95" r="14" fill="#fff" stroke="#555"/><text x="240" y="98" text-anchor="middle" font-size="9">X</text>
        <line x1="240" y1="69" x2="240" y2="81" stroke="#333" marker-end="url(#m2)"/>
        <text x="400" y="18" text-anchor="middle" font-size="10" font-weight="700" fill="#1e4d6b">③ 콜라이더</text>
        <circle cx="365" cy="55" r="14" fill="#fff" stroke="#555"/><text x="365" y="59" text-anchor="middle" font-size="9">X</text>
        <circle cx="435" cy="55" r="14" fill="#fff" stroke="#555"/><text x="435" y="59" text-anchor="middle" font-size="9">Y</text>
        <circle cx="400" cy="95" r="16" fill="#fce4ec" stroke="#8b2942"/><text x="400" y="99" text-anchor="middle" font-size="9">Z</text>
        <line x1="375" y1="65" x2="392" y2="85" stroke="#333" marker-end="url(#m2)"/>
        <line x1="425" y1="65" x2="408" y2="85" stroke="#333" marker-end="url(#m2)"/>
      </svg>

      **그림 2.** 세 가지 대표 구조(개념도). ① 포크(교란), ② 방향이 데이터만으로 식별되지 않음, ③ 콜라이더에 조건화하면 *X*–*Y* 연관이 생길 수 있음(11장에서 심화).

:::

    ## 1.1.5 「통제하면 되지 않나」라는 반론에 대한 답변

      이쯤에서 많은 독자는 이렇게 생각할 것이다. *「그러면 가능한 모든 변수를 통제하면 되지 않나? 고차원 회귀나 정규화(regularization)를 쓰면 해결되는 것 아닌가?」*

    이 직관은 두 가지 이유에서 작동하지 않는다.

      첫째, **측정하지 못한 교란 변수는 통제 자체가 불가능하다.** 우리가 모델에 포함할 수 있는 변수는 이미 데이터에 있는 것뿐이다. 데이터 생성 과정에서 작동한 인과 구조를 우리가 모른다면, 무엇을 통제해야 하는지조차 알 수 없다.

      둘째, **더 많은 변수를 통제하는 것이 언제나 더 나은 인과 추론을 보장하지 않는다.** 위에서 살펴본 것처럼, 콜라이더를 통제하면 오히려 편향이 생긴다. 매개변수(mediator)를 통제하면 총 인과효과가 아닌 직접 효과만을 추정하게 된다. 통제 변수의 선택은 통계적 판단이 아니라 **인과적 판단**의 문제다. 즉, 어떤 변수를 통제할 것인가의 답은 데이터가 아니라 **인과 구조에 대한 사전 지식(prior knowledge of the DAG)**에서 나온다.

      고차원 기계학습 모델도 이 문제에서 자유롭지 않다. LASSO나 신경망은 예측(prediction)에서 탁월하지만, 예측력이 높다고 해서 인과 해석이 가능해지는 것은 아니다. 예측 모델은 *P*(*Y* | *X*)를 잘 추정하도록 최적화되어 있다. 그러나 인과 질문은 *P*(*Y* | do(*X*)), 즉 *X*에 개입했을 때 *Y*의 분포를 묻는다. 이 두 양은 근본적으로 다르며, 데이터만으로는 전자에서 후자를 도출할 수 없다.

    ## 1.1.6 인과 추론이 필요한 이유: 의사결정과 개입

      인과와 상관의 구분이 학문적 엄밀성만의 문제라면, 실용적 관점에서는 그냥 넘어갈 수도 있다. 그러나 이 구분은 의사결정과 정책의 문제에서 생사를 가르기도 한다.

      1950년대, 흡연과 폐암의 상관관계는 이미 데이터에서 명확히 보였다. 담배 회사들은 「이것은 상관일 뿐, 인과가 아니다」라는 주장으로 수십 년간 규제를 막았다. 그 반론이 틀렸음을 밝히기 위해서는 단순한 상관 분석이 아니라 인과 구조에 대한 엄밀한 논증이 필요했다(U.S. Public Health Service, 1964).

      2000년대 초 일부 국가에서는 대형 병원의 수술 후 회복률이 소형 병원보다 낮게 관측된다는 이유로 대형 병원의 예산을 삭감하거나 성과 평가에서 불이익을 주었다. 그러나 이 비교에는 심각한 선택 편향이 내재되어 있다. 중증 환자는 대형 병원으로 집중되는 경향이 있으므로, 중증도(severity)를 통제하지 않은 단순 비교는 대형 병원의 치료 역량을 오히려 과소평가한다. 즉 소형 병원의 높은 회복률은 더 가벼운 환자를 주로 받기 때문일 수 있으며, 이를 「소형 병원이 더 잘 치료한다」는 근거로 사용하는 것은 잘못된 인과 해석이다. 선택 편향을 무시한 상관 기반 정책이 자원 배분의 오류를 낳은 것이다.

      유사한 문제는 미국의 병원 재입원율 감소 프로그램(HRRP)에서도 나타났다. 2012년 도입된 이 정책은 30일 이내 재입원율이 높은 병원의 Medicare 수가를 삭감하는 방식이었고, 표면적으로는 성과 기반 보상처럼 보였다. 그러나 실제로는 저소득층·중증 환자를 주로 담당하는 안전망 병원에 불균형적인 불이익이 집중되었다. 이 병원들의 높은 재입원율은 치료 질의 단순한 반영이라기보다 환자 구성(case mix)의 차이와 강하게 연결되어 있었기 때문이다. 환자 구성이라는 교란 변수를 충분히 보정하지 않은 상관 기반 정책이, 오히려 취약 계층을 더 많이 돌보는 병원에 페널티를 부과하는 역설을 낳은 셈이다.

<svg width="470" height="210" viewBox="0 0 470 210" xmlns="http://www.w3.org/2000/svg" font-family="Pretendard, 'Malgun Gothic', sans-serif">
        <defs>
          <marker id="arr-hosp" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
            <polygon points="0 0, 9 4.5, 0 9" fill="#37474f"/>
          </marker>
        </defs>
        <text x="235" y="22" text-anchor="middle" font-size="12" fill="#1e4d6b" font-weight="700">그림 3. 병원 규모–회복률 비교의 선택 편향 구조</text>

        <circle cx="235" cy="68" r="30" fill="#fff3e0" stroke="#e65100" stroke-width="2"/>
        <text x="235" y="64" text-anchor="middle" font-size="11" font-weight="700" fill="#333">
          <tspan font-style="italic">S</tspan>
        </text>
        <text x="235" y="79" text-anchor="middle" font-size="9.5" fill="#333">중증도</text>

        <circle cx="115" cy="148" r="30" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
        <text x="115" y="144" text-anchor="middle" font-size="11" font-weight="700" fill="#333">
          <tspan font-style="italic">H</tspan>
        </text>
        <text x="115" y="159" text-anchor="middle" font-size="9.5" fill="#333">병원 규모</text>

        <circle cx="355" cy="148" r="30" fill="#e8f5ef" stroke="#1d6b4a" stroke-width="2"/>
        <text x="355" y="144" text-anchor="middle" font-size="11" font-weight="700" fill="#333">
          <tspan font-style="italic">Y</tspan>
        </text>
        <text x="355" y="159" text-anchor="middle" font-size="9.5" fill="#333">회복률</text>

        <line x1="218" y1="92" x2="135" y2="124" stroke="#37474f" stroke-width="2" marker-end="url(#arr-hosp)"/>
        <line x1="252" y1="92" x2="335" y2="124" stroke="#37474f" stroke-width="2" marker-end="url(#arr-hosp)"/>

        <line x1="145" y1="148" x2="325" y2="148" stroke="#90a4ae" stroke-width="1.5" stroke-dasharray="6 5"/>
        <text x="235" y="141" text-anchor="middle" font-size="8.5" fill="#78909c">중증도 미통제 시 관측 상관</text>

        <text x="235" y="194" text-anchor="middle" font-size="9.5" fill="#546e7a">
          <tspan font-style="italic">S</tspan><tspan>가 </tspan><tspan font-style="italic">H</tspan><tspan>와 </tspan><tspan font-style="italic">Y</tspan><tspan>의 공통 원인이므로, </tspan>
          <tspan font-style="italic">H</tspan><tspan>–</tspan><tspan font-style="italic">Y</tspan><tspan> 단순 비교는 선택 편향을 포함</tspan>
        </text>
      </svg>

      **그림 3.** 중증도(*S*)가 병원 규모 선택(*H*)과 회복률(*Y*)에 동시에 영향을 줄 때, *S*를 통제하지 않은 *H*–*Y* 비교는 인과효과와 선택 편향이 섞인다.

:::

      이처럼 우리가 실제로 알고 싶은 것은 대부분 **개입(intervention)**의 효과다. 이 약을 투여하면 회복률이 높아지는가? 이 정책을 시행하면 고용률이 오르는가? 이 기능을 추가하면 사용자 유지율이 개선되는가? 이러한 질문들은 본질적으로 반사실(counterfactual)의 언어를 요구한다. 개입하지 않았다면 어떻게 되었을까? 이 질문에 상관은 답하지 못한다.

    ## 1.1.7 그렇다면 무엇이 필요한가
    상관과 인과의 간극을 메우려면 세 가지가 필요하다.

      첫째, **인과 질문을 수학적으로 표현하는 언어**가 필요하다. 이를 위해 이 책은 잠재결과(potential outcomes) 프레임과 구조 인과 모형(structural causal model, SCM)이라는 두 가지 언어를 사용한다. 이 두 언어는 서로 다른 직관을 강조하지만, 엄밀하게는 동치임을 나중에 보일 것이다.

      둘째, **인과효과가 데이터로부터 원칙적으로 계산 가능한지 판별하는 기준**, 즉 식별(identification) 이론이 필요하다. 어떤 가정 하에서, 어떤 통계량이 인과효과와 일치하는가를 묻는 것이 식별 문제다.

      셋째, **식별된 인과효과를 유한 표본에서 효율적으로 추정하는 방법론**, 즉 추정(estimation) 전략이 필요하다. 이 책의 4부와 6부가 주로 이 문제를 다룬다.

      회귀는 세 번째 도구, 즉 추정의 도구로서 여전히 유용하다. 문제는 회귀가 첫 번째와 두 번째를 대신할 수 없다는 점이다. 인과 질문을 명확히 하고, 그 질문이 식별 가능한 조건을 확보한 뒤에야 회귀는 비로소 인과 추론의 도구가 된다. **이것이 이 책 전체의 논리 구조다.**


:::
summary

      핵심 요약

        - 데이터는 조건부 분포 *P*(*Y* | *X*)를 알려주지만, 인과 질문은 개입 분포 *P*(*Y* | do(*X*))를 요구한다. 이 두 양은 교란·역인과·콜라이더 편향이 존재할 때 다르다.

        - 회귀는 인과 가정이 사전에 정당화될 때만 인과적으로 해석 가능하며, 그 가정 자체를 데이터로 검증할 수 없다.

        - 더 많은 변수를 통제하는 것이 항상 더 나은 인과 추론을 의미하지는 않는다. 통제 변수의 선택은 인과 구조에 대한 사전 지식의 문제다.

        - 인과 추론은 ① 인과 질문의 형식화, ② 식별 가능성의 판별, ③ 효율적 추정의 세 단계로 이루어지며, 회귀는 세 번째 단계의 도구 중 하나다.

:::

      다음 절([1.2 반사실의 정의와 직관적 예시](ch01-02-counterfactuals.html))에서는 이 간극을 메우기 위한 첫 번째 언어인 반사실(counterfactual)의 수학적 정의를 소개하고, [인과 사다리(ladder of causation)](ch01-03-ladder.html)를 통해 인과 질문의 세 층위를 체계화한다.
