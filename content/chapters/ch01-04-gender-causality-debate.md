---
title: 1.4 성별은 원인이 될 수 없는가 — 비판적 검토
description: Holland(1986)의 “No causation without manipulation” 원칙은 인과추론의 엄밀성을 강화했지만, 성별·인종·계층 같은 사회적 속성을 어떻게 다뤄야 하는지에 대해 큰 논쟁을 낳았다. 이 절은 해당 논쟁을 방법론·철학·정책 관점에서 균형 있게 정리한다.
---

# 1.4 성별은 원인이 될 수 없는가 — 비판적 검토

Holland(1986)의 **“No causation without manipulation”** 원칙은 인과추론의 엄밀성을 강화했지만,
      성별·인종·계층 같은 사회적 속성을 어떻게 다뤄야 하는지에 대해 큰 논쟁을 낳았다.
      이 절은 해당 논쟁을 방법론·철학·정책 관점에서 균형 있게 정리한다.

    ## 1.4.1 Holland의 원래 주장

      Holland는 “원인(cause)”을 단위에 잠재적으로 노출 가능한 처치로 본다. 이 기준에서 성별은 속성(attribute)이므로
      동일 단위에서 처치처럼 바꾸기 어렵고, 따라서 잠재결과 차이를 직접 정의하기 어렵다.

    \[
      \text{원인} \iff \text{잠재적 노출 가능(potentially exposable)}
    \]

:::

    \[
      \text{성별 속성 }A_i\ \Rightarrow\ \text{동일 단위에서 }Y_i(1),Y_i(0)\text{ 비교의 해석이 불명확}
    \]

:::


:::
example

      **예시.** “그녀가 여성이라 시험을 잘 봤다”는 문장은 같은 개인을 남성으로 바꾼 잠재결과를 어떻게 정의할지 모호하다.
      반면 “추가 코칭을 받았기 때문에 성적이 올랐다”는 문장은 코칭 여부를 처치로 정의해 비교할 수 있다.

:::

    ## 1.4.2 비판 1 — 처치 정의가 너무 협소한가

      VanderWeele &amp; Hernán(2012)의 핵심은 “성별 전체” 대신 **조작 가능한 측면**을 정의하라는 것이다.
      예를 들어 이력서 실험에서 이름 신호를 무작위화하면 인식된 성별 신호의 효과를 정의할 수 있다.

    \[
      T_i=
      \begin{cases}
      1 & \text{여성으로 인식되는 이름 신호}\\
      0 & \text{남성으로 인식되는 이름 신호}
      \end{cases},
      \qquad
      \Delta = E[Y_i(1)-Y_i(0)].
    \]

:::

      결론은 “성별 효과는 원천적으로 불가능”이 아니라 “**어떤 측면을 처치로 정의하는지 명시하라**”이다.


:::
example

      **예시.** 동일 이력서에 이름만 바꿔 제출했을 때 콜백률이 다르면, 이것은 “성별 전체 효과”가 아니라
      “인식된 성별 신호”의 효과다. 정책적으로는 블라인드 채용 도입의 근거가 된다.

:::

    ## 1.4.3 비판 2 — 조작 가능성은 필요조건인가

      Woodward(2003)는 실제 조작 가능성보다 개념적 개입 가능성을 강조한다.
      현실에서 직접 조작이 어려운 변수라도, 반사실적으로 일관된 개입 개념을 둘 수 있으면 인과 진술이 가능하다는 입장이다.

    \[
      \text{Holland: 실제 조작 가능성 중심}\qquad
      \text{Woodward: 개념적 개입 가능성 중심}
    \]

:::


:::
example

      **예시.** 소행성 충돌의 원인 효과나 출생 연도의 거시경제 효과는 실험으로 조작할 수 없지만,
      역사 비교와 구조모형을 통해 인과 질문 자체를 무의미하다고 보지는 않는다.

:::

    ## 1.4.4 비판 3 — 사회과학의 구조적 원인

      Sen, Krieger 등의 논의는 조작가능성 기준을 엄격하게만 적용하면 사회적 불평등의 핵심 질문이 분석 밖으로 밀려난다고 비판한다.
      Pearl의 SCM 관점에서도 3층 반사실 질문은 조작 가능성만으로 환원되지 않는다.

    \[
      P\!\left(Y_{g'}=y'\mid G=g,\;Y=y\right)
    \]

:::

      다만 해석 가능성을 확보하려면 \(G\) 자체보다 제도·규범·노동시장 경로 같은 매개를 함께 구조화해야 한다.


:::
example

      **예시.** 성별 임금격차 연구에서 “성별 자체”보다 채용 차별, 승진 기준, 돌봄 공백 같은
      경로 변수의 개입 효과를 추정하면 정책 설계와 직접 연결된다.

:::

    ## 1.4.5 비판 4 — 처치 버전 문제는 보편적이다

      Hernán(2016)은 “음주”, “운동”, “식이” 같은 전형적 처치도 버전(version) 문제를 갖는다고 지적한다.
      따라서 성별 사례의 쟁점은 특수 사례라기보다 복잡한 처치 전반의 정밀화 문제로 봐야 한다.


:::
example

      **예시.** “운동의 효과”는 유산소/근력, 강도, 주당 빈도에 따라 달라진다.
      즉 조작 가능하다는 이유만으로 자동으로 인과질문이 명확해지지는 않는다.

:::

    ## 1.4.6 비판 5 — 메커니즘과 총효과

      Robins &amp; Greenland(1992)는 잠재결과 평균 차이만으로 메커니즘 정보를 충분히 포착하기 어렵다고 지적한다.
      성별과 임금의 관계는 교육·직업선택·차별·돌봄부담 등의 경로를 통해 작동하므로, 총효과와 경로효과를 분해해 해석해야 한다.

    \[
      \text{총효과(개념적)}=E[W\mid do(G=g_1)]-E[W\mid do(G=g_0)].
    \]

:::

<svg width="520" height="220" viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg">
        <text x="260" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#1e4d6b">성별-임금 논쟁의 단순 DAG (개념도)</text>

        <circle cx="90" cy="85" r="26" fill="#fff" stroke="#1e4d6b" stroke-width="2"/>
        <text x="90" y="90" text-anchor="middle" font-size="11">성별 G</text>

        <rect x="180" y="48" width="120" height="44" rx="8" fill="#eef3f6" stroke="#1e4d6b"/>
        <text x="240" y="75" text-anchor="middle" font-size="10.5">교육/전공 M1</text>

        <rect x="180" y="110" width="120" height="44" rx="8" fill="#eef3f6" stroke="#1e4d6b"/>
        <text x="240" y="137" text-anchor="middle" font-size="10.5">채용/승진 M2</text>

        <rect x="180" y="168" width="120" height="34" rx="8" fill="#eef3f6" stroke="#1e4d6b"/>
        <text x="240" y="189" text-anchor="middle" font-size="10.5">돌봄부담 M3</text>

        <circle cx="410" cy="120" r="28" fill="#fff" stroke="#1d6b4a" stroke-width="2"/>
        <text x="410" y="125" text-anchor="middle" font-size="11">임금 W</text>

        <rect x="330" y="20" width="150" height="44" rx="8" fill="#fff7ea" stroke="#a06b1a" stroke-width="1.8"/>
        <text x="405" y="38" text-anchor="middle" font-size="10.5" font-weight="600">정책개입 P</text>
        <text x="405" y="53" text-anchor="middle" font-size="9.5">차별금지·돌봄지원</text>

        <line x1="116" y1="76" x2="178" y2="70" stroke="#333" stroke-width="1.6" marker-end="url(#arr14)"/>
        <line x1="113" y1="93" x2="178" y2="126" stroke="#333" stroke-width="1.6" marker-end="url(#arr14)"/>
        <line x1="106" y1="106" x2="178" y2="182" stroke="#333" stroke-width="1.6" marker-end="url(#arr14)"/>
        <line x1="116" y1="88" x2="382" y2="115" stroke="#7b7b7b" stroke-width="1.3" stroke-dasharray="5 3" marker-end="url(#arr14)"/>

        <line x1="300" y1="70" x2="381" y2="108" stroke="#333" stroke-width="1.6" marker-end="url(#arr14)"/>
        <line x1="300" y1="132" x2="381" y2="121" stroke="#333" stroke-width="1.6" marker-end="url(#arr14)"/>
        <line x1="300" y1="184" x2="382" y2="132" stroke="#333" stroke-width="1.6" marker-end="url(#arr14)"/>

        <line x1="377" y1="64" x2="272" y2="106" stroke="#a06b1a" stroke-width="1.5" marker-end="url(#arrP)"/>
        <line x1="395" y1="64" x2="256" y2="168" stroke="#a06b1a" stroke-width="1.5" marker-end="url(#arrP)"/>
        <line x1="416" y1="64" x2="410" y2="90" stroke="#a06b1a" stroke-width="1.5" marker-end="url(#arrP)"/>

        <text x="332" y="154" font-size="9" fill="#666">점선: 직접효과 가설</text>

        <defs>
          <marker id="arr14" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
            <polygon points="0 0, 8 4, 0 8" fill="#333"/>
          </marker>
          <marker id="arrP" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
            <polygon points="0 0, 8 4, 0 8" fill="#a06b1a"/>
          </marker>
        </defs>
      </svg>

      **그림.** 성별 \(G\)가 매개 경로 \(M_1,M_2,M_3\)를 통해 임금 \(W\)에 영향을 주고, 정책개입 \(P\)는 매개와 결과 노드에 개입한다는 직관적 구조.

:::


:::
example

      **예시.** 동일 학력 집단에서 성별 임금격차가 관측될 때,
      채용 단계 편향과 경력 단절 경로를 나눠 보면 정책 처방(채용 규칙 개선 vs 돌봄 지원)이 달라진다.

:::

    ## 1.4.7 Holland 원칙의 재평가

<table class="comp-table" role="table" aria-label="Holland 원칙의 가치와 한계">
      <thead>
        <tr>
          <th scope="col">측면</th>
          <th scope="col">가치</th>
          <th scope="col">한계</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>개념적 엄밀성</td>
          <td>처치 정의를 명확히 하도록 강제</td>
          <td>존재론으로 확장하면 과도한 배제 가능</td>
        </tr>
        <tr>
          <td>정책 연결성</td>
          <td>개입 가능한 변수 중심의 권고 제시 가능</td>
          <td>구조적 불평등 원인을 축소 해석할 위험</td>
        </tr>
        <tr>
          <td>반사실 해석</td>
          <td>동일 단위 비교의 엄격성 유지</td>
          <td>복잡한 사회적 정체성 문제를 단순화하기 어려움</td>
        </tr>
      </tbody>
    </table>

    ## 1.4.8 비판에 대한 비판(재반론)

      Holland 비판에도 다시 비판이 가능하다. 첫째, “개념적 개입 가능성”은 너무 넓어
      검증 불가능한 가정이 늘어날 위험이 있다. 둘째, “성별의 총효과”는 수학적으로 쓸 수 있어도
      정책 처치로 번역할 때 의미가 흐려질 수 있다. 셋째, 구조적 원인을 강조하는 연구도
      측정·식별 전략이 약하면 규범적 주장만 남을 수 있다.

      즉 재반론의 핵심은 단순하다. **질문 확장**은 필요하지만,
      그만큼 **처치 정의·식별 가정·검증 가능성**을 더 엄격히 관리해야 한다는 것이다.
      이 점에서 Holland의 경고는 여전히 유효한 품질 통제 장치로 기능한다.

    ## 1.4.9 종합

      현대 합의에 가까운 해석은 다음과 같다.
      (i) Holland 원칙은 강력한 **방법론적 규율**이다.
      (ii) 그러나 “성별은 결코 원인이 아니다”라는 강한 존재론으로 일반화하면 한계가 있다.
      (iii) 실무적으로는 성별의 특정 측면과 개입 가능한 경로를 분해해 질문을 정밀화하는 것이 가장 생산적이다.


:::
summary

      핵심 요약

        - Holland의 원칙은 인과 질문의 정밀화를 돕는 강력한 규칙이다.

        - 성별 논쟁의 핵심은 “가능/불가능” 이분법보다 처치 정의의 해상도다.

        - 조작 가능성은 정책 인과에서 특히 유용하지만, 인과의 유일한 존재론 기준은 아니다.

        - SCM 반사실 언어는 구조적 원인을 더 넓게 서술할 수 있지만, 가정과 해석 책임이 커진다.

        - 비판을 수용하더라도 식별 가능성과 정책 번역 가능성을 함께 점검해야 한다.

:::
