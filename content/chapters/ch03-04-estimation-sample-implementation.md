---
title: 3.4 추정: 식별된 표현의 표본 구현
description: 추정은 식별된 인과량의 모집단 표현을 유한 표본에서 계산하는 과정이다. 이 절은 식별과 추정의 차이를 유지하면서, 표본 구현과 진단의 의미를 설명한다.
---

# 3.4 추정: 식별된 표현의 표본 구현
식별이 “원리적으로 계산 가능한가”의 문제였다면, 추정은 “표본으로 얼마나 안정적으로 계산할 수 있는가”의 문제다. 이 구분은 단순해 보이지만 매우 중요하다. 식별된 인과량을 잘못 구현하면 불안정한 추정이나 과도한 가중치, 모델 의존성 때문에 실증결과가 크게 흔들릴 수 있기 때문이다.

## 3.4 추정: 식별된 표현의 표본 구현

      추정 단계의 목표는 “예측 정확도 최대화”가 아니라, 식별된 estimand를 편향-분산 균형 하에서 안정적으로 계산하는 것이다.
      따라서 추정량 선택은 질문(ATE/ATT/LATE), 자료구조, 양의성 위반 여부에 따라 달라진다.

    \[
      \theta = E\!\left[E(Y\mid D=1,X)-E(Y\mid D=0,X)\right],\qquad
      \hat\theta_{AIPW}=\frac{1}{n}\sum_{i=1}^n\left[\hat\mu_1(X_i)-\hat\mu_0(X_i)+\frac{D_i(Y_i-\hat\mu_1(X_i))}{\hat e(X_i)}-\frac{(1-D_i)(Y_i-\hat\mu_0(X_i))}{1-\hat e(X_i)}\right].
    \]

:::

      AIPW는 outcome model 또는 propensity model 중 하나가 맞으면 일치성을 갖는 이중강건 추정량의 대표 예다.
      최근에는 교차적합(cross-fitting)을 결합해 고차원/ML 환경에서도 점근정규성을 확보한다.

    ## 연구 사례: 실업훈련 프로그램 평가

      Lalonde(1986) 이후 재고용 프로그램 평가는 “실험 결과를 관측자료 추정기가 재현하는가”를 테스트베드로 사용해 왔다.
      같은 식별식이라도 매칭·IPW·AIPW·DML의 유한표본 성능이 달라질 수 있고, 공통지지 부족 구간에서 추정 불안정이 크게 증가한다.

<svg width="520" height="170" viewBox="0 0 520 170" xmlns="http://www.w3.org/2000/svg">
        <text x="260" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#1e4d6b">추정 워크플로우</text>
        <rect x="25" y="35" width="110" height="44" rx="7" fill="#eef3f6" stroke="#1e4d6b"/><text x="80" y="62" text-anchor="middle" font-size="10.5">식별식 확정</text>
        <rect x="155" y="35" width="110" height="44" rx="7" fill="#eef3f6" stroke="#1e4d6b"/><text x="210" y="62" text-anchor="middle" font-size="10.5">모형 적합</text>
        <rect x="285" y="35" width="110" height="44" rx="7" fill="#eef3f6" stroke="#1e4d6b"/><text x="340" y="62" text-anchor="middle" font-size="10.5">교차적합</text>
        <rect x="415" y="35" width="80" height="44" rx="7" fill="#eef3f6" stroke="#1e4d6b"/><text x="455" y="62" text-anchor="middle" font-size="10.5">추정값</text>
        <line x1="136" y1="57" x2="153" y2="57" stroke="#333" marker-end="url(#m34)"/>
        <line x1="266" y1="57" x2="283" y2="57" stroke="#333" marker-end="url(#m34)"/>
        <line x1="396" y1="57" x2="413" y2="57" stroke="#333" marker-end="url(#m34)"/>
        <rect x="155" y="100" width="240" height="50" rx="8" fill="#fff7ea" stroke="#a06b1a"/>
        <text x="275" y="121" text-anchor="middle" font-size="10.5">진단: 공통지지 · 극단가중치 · 민감도</text>
        <text x="275" y="139" text-anchor="middle" font-size="10.5">보고: 점추정 + 불확실성 + 가정 위반 가능성</text>
        <defs><marker id="m34" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#333"/></marker></defs>
      </svg>

      **그림 3.4.** 추정은 계산만이 아니라 진단·보고 규율을 포함한다.

:::

      이제 3장의 마지막 절에서는 왜 이 구분이 이후 장 전체의 공통 문법이 되는지, 즉 백도어 조정, IV, RDD, DiD 같은 서로 다른 전략을 같은 틀로 비교해야 하는 이유를 정리한다.
