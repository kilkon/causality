---
title: 3.5 왜 이 구분이 필요한가
description: 설정, 식별, 추정의 구분은 이후 장들의 공통 비교 언어가 된다. 이 절은 왜 같은 숫자라도 서로 다른 식별 전략과 추정 목표를 가질 수 있는지 정리한다.
---

# 3.5 왜 이 구분이 필요한가

3장을 마무리하는 핵심 메시지는 분명하다. 인과연구를 추정기 이름으로만 읽으면 논점이 섞이지만, 설정-식별-추정의 언어로 읽으면 서로 다른 방법이 무엇을 가정하고 무엇을 포기하는지 훨씬 명확하게 보인다. 그래서 이 구분은 단지 3장 안의 개념 구분이 아니라, 이후 책 전체를 읽는 공통 문법이 된다.

## 3.5 왜 이 구분이 필요한가

      4장 이후에는 서로 다른 설계(백도어 조정, IV, RDD, DiD)를 비교해야 한다. 이때 비교 단위를 “추정기 이름”으로 두면
      논점이 섞인다. 비교 단위를 **설정-식별-추정**으로 고정하면, 각 방법이 무엇을 가정하고 무엇을 포기하는지 명확해진다.

    ## 연구 사례: 교육연수와 임금

      같은 질문(교육연수가 임금에 미치는 효과)도 설계에 따라 estimand가 달라진다.
      OLS는 조건부 독립 가정 하 ATE 근사, IV(출생분기·근접대학 도구)는 LATE, RDD(장학금 컷오프)는 cutoff 근처 국소효과를 준다.
      즉 “숫자”가 다르면 누가 틀렸다는 뜻이 아니라, 대개 **질문 대상 집단이 다르다**는 뜻이다.

<svg width="520" height="170" viewBox="0 0 520 170" xmlns="http://www.w3.org/2000/svg">
        <text x="260" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#1e4d6b">동일 질문, 다른 식별 설계</text>
        <rect x="30" y="40" width="140" height="48" rx="8" fill="#eef3f6" stroke="#1e4d6b"/><text x="100" y="60" text-anchor="middle" font-size="11">OLS/조정</text><text x="100" y="76" text-anchor="middle" font-size="10">조건부 독립</text>
        <rect x="190" y="40" width="140" height="48" rx="8" fill="#edf7ef" stroke="#1d6b4a"/><text x="260" y="60" text-anchor="middle" font-size="11">IV</text><text x="260" y="76" text-anchor="middle" font-size="10">외생성·배제</text>
        <rect x="350" y="40" width="140" height="48" rx="8" fill="#f6eef8" stroke="#6b4c9a"/><text x="420" y="60" text-anchor="middle" font-size="11">RDD</text><text x="420" y="76" text-anchor="middle" font-size="10">연속성</text>
        <line x1="100" y1="89" x2="100" y2="120" stroke="#333" marker-end="url(#m35)"/>
        <line x1="260" y1="89" x2="260" y2="120" stroke="#333" marker-end="url(#m35)"/>
        <line x1="420" y1="89" x2="420" y2="120" stroke="#333" marker-end="url(#m35)"/>
        <text x="100" y="138" text-anchor="middle" font-size="10">ATE(가정하)</text>
        <text x="260" y="138" text-anchor="middle" font-size="10">LATE</text>
        <text x="420" y="138" text-anchor="middle" font-size="10">국소효과</text>
        <defs><marker id="m35" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#333"/></marker></defs>
      </svg>

      **그림 3.5.** 설계가 다르면 같은 정책 질문에서도 식별되는 효과가 다를 수 있다.

:::


:::
summary

      핵심 요약

        - 3장의 구분은 “방법 선택”을 “질문-가정-대상집단” 언어로 번역해 준다.

        - 서로 다른 추정값은 종종 충돌이 아니라 서로 다른 estimand의 반영이다.

        - 연구 보고서는 반드시 식별 가정, 표적 estimand, 추정 불확실성을 함께 제시해야 한다.

:::

      확장 읽기: 전체 비교표와 용어 대응은 [3.1 모형 설정, 식별, 추정](../ch03-01-specification-identification-estimation.html)를 참고한다.

      다음 장에서는 이 틀을 DAG의 경로 규칙과 결합해, 편향의 구조와 식별 규칙을 그림으로 읽는 방법을 다룬다.
