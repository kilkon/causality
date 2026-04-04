---
title: 3.2 SCM·DAG에서의 모형 설정
description: 모형 설정은 단순한 회귀식 선택이 아니라 어떤 구조를 허용하고 어떤 경로를 배제할지를 정하는 일이다. 이 절은 SCM과 DAG 언어로 모형 설정의 의미를 설명한다.
---

# 3.2 SCM·DAG에서의 모형 설정

3.1절에서 모형 설정, 식별, 추정을 구분했다면, 이제 첫 단계인 모형 설정이 실제로 무엇을 뜻하는지 더 구체적으로 볼 차례다. SCM과 DAG는 연구자가 어떤 변수 간 구조를 가정하고 있는지를 시각적·형식적으로 드러내 주는 도구다. 즉 모형 설정은 “식 하나를 쓰는 일”이 아니라, 어떤 화살표를 허용하고 어떤 경로를 배제할지를 정하는 일이다.

## 1. DAG란 무엇인가
      **DAG**는 *directed acyclic graph*(방향 비순환 그래프)의 약자이다. 변수(또는 모형의 양)를 **노드**로 두고, 한 노드에서 다른 노드로 향하는 **방향간선(화살표)**으로 직접 인과(또는 직접 의존)를 표시한다. 화살표 방향만 따라 이동할 때 어떤 노드에서 출발해 다시 그 노드로 돌아오는 경로가 없도록 **순환(cycle)**이 없어야 한다.

<svg width="320" height="130" viewBox="0 0 320 130" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arr" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
              <polygon points="0 0, 10 3, 0 6" fill="#1e4d6b"/>
            </marker>
          </defs>
          <circle cx="55" cy="65" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="55" y="72" text-anchor="middle" font-size="17" font-weight="600">A</text>
          <line x1="81" y1="65" x2="129" y2="65" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr)"/>
          <circle cx="155" cy="65" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="155" y="72" text-anchor="middle" font-size="17" font-weight="600">B</text>
          <line x1="181" y1="65" x2="229" y2="65" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr)"/>
          <circle cx="255" cy="65" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="255" y="72" text-anchor="middle" font-size="17" font-weight="600">C</text>
        </svg>

        그림 1. 단순한 사슬(chain)의 연장: \(A \rightarrow B \rightarrow C\). 순환이 없으므로 DAG 조건을 만족한다.

:::

      ## 2. DAG를 구성하는 요소

        - **노드(node)**: 통상 하나의 무작위 변수(관측·잠재, 처치, 결과, 공변량 등)에 대응한다.

        - **방향간선**: \(A \rightarrow B\)는 “\(A\)가 \(B\)의 직접 원인(또는 \(B\)의 직접 부모)”이라는 가정이다. **없는 화살표**는 직접 연결이 없다는 **배제** 가정이다.

        - **비순환성**: 동시성·균형 피드백 등은 단일 시점 DAG만으로 표현하기 어려울 수 있어, 시점별 노드나 다른 도구가 필요할 수 있다.

        - **부모·자식·경로**: \(B\)로 들어오는 화살표의 출발점이 \(B\)의 부모; 나가는 화살표의 끝이 자식이다. 간선을 따라 이은 노드의 열이 **경로**이다.

      ## 3. 세 가지 기본 구형(three elementary configurations)
      인과 그래프를 읽을 때 반복되는 국소 패턴으로, **사슬(chain)**, **갈래(fork)**, **역갈래(inverted fork)**가 대표적이다. 영문 문헌에서는 각각 head-to-tail, common cause(confounder), collider 구조와 연결하여 설명하는 경우가 많다.

      ### 3.1 사슬(chain): \(A \rightarrow B\), \(A \rightarrow C \rightarrow B\) 등
      화살표가 **머리에서 꼬리로** 이어지는 연속이다. \(A \rightarrow B\)는 \(A\)의 직접 효과만을 나타낸다. \(A \rightarrow C \rightarrow B\)에서는 \(C\)가 **매개변수(mediator)** 역할을 하며, \(A\)에서 \(B\)로 가는 **간접 경로**가 생긴다. 연관은 방향 경로를 따라 전파될 수 있다. 매개변수에 대한 조건부 독립·통제 여부는 식별(예: 자연직접·간접효과 분해)과 밀접하다.

<svg width="300" height="120" viewBox="0 0 300 120" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arr2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
              <polygon points="0 0, 10 3, 0 6" fill="#1e4d6b"/>
            </marker>
          </defs>
          <circle cx="70" cy="60" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="70" y="67" text-anchor="middle" font-size="18" font-weight="600">A</text>
          <line x1="98" y1="60" x2="182" y2="60" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr2)"/>
          <circle cx="230" cy="60" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="230" y="67" text-anchor="middle" font-size="18" font-weight="600">B</text>
        </svg>

        그림 2. 길이 1의 사슬: \(A \rightarrow B\).

:::

<svg width="380" height="120" viewBox="0 0 380 120" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arr3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
              <polygon points="0 0, 10 3, 0 6" fill="#1e4d6b"/>
            </marker>
          </defs>
          <circle cx="60" cy="60" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="60" y="67" text-anchor="middle" font-size="17" font-weight="600">A</text>
          <line x1="86" y1="60" x2="144" y2="60" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr3)"/>
          <circle cx="190" cy="60" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="190" y="67" text-anchor="middle" font-size="17" font-weight="600">C</text>
          <line x1="216" y1="60" x2="274" y2="60" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr3)"/>
          <circle cx="320" cy="60" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="320" y="67" text-anchor="middle" font-size="17" font-weight="600">B</text>
        </svg>

        그림 3. 길이 2의 사슬(매개): \(A \rightarrow C \rightarrow B\).

:::

      ### 3.2 갈래(fork): \(A \leftarrow C \rightarrow B\)
      한 노드 \(C\)에서 **두 갈래**로 화살표가 나간다. \(C\)는 \(A\)와 \(B\)의 **공통 원인(common cause)**이며, 관측연구에서 전형적인 **교란(confounding)** 구조로 그린다. \(A\)와 \(B\) 사이에 직접 화살표가 없어도 \(C\)를 통한 **비인과 경로** \(A \leftarrow C \rightarrow B\)가 있으면 한쪽 변동이 다른 쪽과 연관될 수 있다. \(C\)를 통제(또는 적절히 무작위화하여 \(C\)와 처치를 독립)하는 전략이 백도어 조정의 직관과 연결된다.

<svg width="320" height="160" viewBox="0 0 320 160" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arr4" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
              <polygon points="0 0, 10 3, 0 6" fill="#1e4d6b"/>
            </marker>
          </defs>
          <circle cx="160" cy="45" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="160" y="52" text-anchor="middle" font-size="18" font-weight="600">C</text>
          <line x1="140" y1="68" x2="85" y2="118" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr4)"/>
          <line x1="180" y1="68" x2="235" y2="118" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr4)"/>
          <circle cx="70" cy="130" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="70" y="137" text-anchor="middle" font-size="18" font-weight="600">A</text>
          <circle cx="250" cy="130" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="250" y="137" text-anchor="middle" font-size="18" font-weight="600">B</text>
        </svg>

        그림 4. 포크(공통 원인): \(A \leftarrow C \rightarrow B\).

:::

      ### 3.3 역갈래(inverted fork): \(A \rightarrow C \leftarrow B\)
      두 화살표가 한 노드 \(C\)에 **들어오는** 형태이다. \(C\)는 **충돌변수(collider)**라 부르며, 영문 “inverted fork”가 가리키는 구형과 일치한다. \(A\)와 \(B\) 사이에는 방향 경로가 없으므로, 그래프가 함의하는 바에 따르면(추가 구조 없이) \(A\)와 \(B\)는 **주변적으로 독립**할 수 있다. 그러나 \(C\) 또는 \(C\)의 자손에 **조건을 걸면**(통제·표본 선택·층화 등) \(A\)와 \(B\) 사이에 **인과가 아닌 연관**이 열릴 수 있다. 이는 선택편향·버크슨 편향의 그래프적 표현과 연결된다.

<svg width="320" height="160" viewBox="0 0 320 160" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arr5" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
              <polygon points="0 0, 10 3, 0 6" fill="#1e4d6b"/>
            </marker>
          </defs>
          <circle cx="70" cy="130" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="70" y="137" text-anchor="middle" font-size="18" font-weight="600">A</text>
          <circle cx="250" cy="130" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="250" y="137" text-anchor="middle" font-size="18" font-weight="600">B</text>
          <line x1="95" y1="118" x2="140" y2="68" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr5)"/>
          <line x1="225" y1="118" x2="180" y2="68" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr5)"/>
          <circle cx="160" cy="45" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="160" y="52" text-anchor="middle" font-size="18" font-weight="600">C</text>
        </svg>

        그림 5. 역갈래(충돌변수): \(A \rightarrow C \leftarrow B\).

:::

        **요약.** 사슬은 인과 전파·매개를, 갈래는 공통 원인·교란을, 역갈래는 충돌변수에서의 조건부 연관(통제·선택에 따른 비인과 경로 개방)을 시각화한다. 복잡한 DAG는 이 세 패턴의 조합으로 읽는다.

:::

# 3.2 SCM·DAG에서의 모형 설정

## 3.2 SCM·DAG에서의 모형 설정

      모형 설정은 “그럴듯한 회귀식”을 고르는 작업이 아니라, **인과 메커니즘을 수학 객체로 명시**하는 작업이다.
      SCM은 그 메커니즘을 방정식으로, DAG는 화살표 구조로 표현한다.

    \[
      \mathcal{M}=\langle \mathbf{U},\mathbf{V},\mathcal{F},P(\mathbf{U})\rangle,\qquad
      V_j=f_j(\mathrm{Pa}(V_j),U_j).
    \]

:::

      여기서 \(\mathrm{Pa}(V_j)\)는 \(V_j\)의 부모 노드(직접 원인)다. 즉 DAG의 화살표 하나는
      “예측 상관”이 아니라 “구조 방정식에서 직접 입력으로 들어가는 변수”라는 가정이다.
      따라서 **화살표를 그린다**는 것은 통계 모형 선택이 아니라 과학적 주장(배제 가정 포함)을 선언하는 일이다.

    ## DAG의 기본 문법 (dag.html 요약 반영)

      DAG는 노드(변수)와 방향간선(직접 인과)을 사용하며, 순환이 없어야 한다.
      핵심은 세 가지 경로 원형이다.

      - **사슬(chain)**: \(A \rightarrow C \rightarrow B\) — 매개 경로, \(C\)를 통제하면 경로가 차단될 수 있다.

      - **포크(fork)**: \(A \leftarrow C \rightarrow B\) — 공통원인(교란), \(C\)를 통제해 백도어를 차단한다.

      - **콜라이더(collider)**: \(A \rightarrow C \leftarrow B\) — 기본적으로 경로가 닫혀 있으나 \(C\)를 조건화하면 오히려 경로가 열린다.

      이 세 원형을 잘못 읽으면 모형 설정 단계에서 바로 오류가 난다. 특히 콜라이더 통제는
      “통제를 많이 할수록 좋다”는 직관을 깨는 대표적 함정이다.
      자세한 도식은 [DAG 보충 노트](../dag.html)를 함께 참고하라.

<svg width="520" height="190" viewBox="0 0 520 190" xmlns="http://www.w3.org/2000/svg">
        <text x="260" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#1e4d6b">경로 원형과 통제 규칙</text>
        <text x="90" y="42" text-anchor="middle" font-size="10.5" fill="#333">사슬</text>
        <circle cx="50" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="50" y="74" text-anchor="middle" font-size="10">A</text>
        <circle cx="90" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="90" y="74" text-anchor="middle" font-size="10">C</text>
        <circle cx="130" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="130" y="74" text-anchor="middle" font-size="10">B</text>
        <line x1="64" y1="70" x2="76" y2="70" stroke="#333" marker-end="url(#arr32)"/>
        <line x1="104" y1="70" x2="116" y2="70" stroke="#333" marker-end="url(#arr32)"/>

        <text x="260" y="42" text-anchor="middle" font-size="10.5" fill="#333">포크(교란)</text>
        <circle cx="220" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="220" y="74" text-anchor="middle" font-size="10">A</text>
        <circle cx="260" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="260" y="74" text-anchor="middle" font-size="10">C</text>
        <circle cx="300" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="300" y="74" text-anchor="middle" font-size="10">B</text>
        <line x1="260" y1="56" x2="232" y2="66" stroke="#333" marker-end="url(#arr32)"/>
        <line x1="260" y1="56" x2="288" y2="66" stroke="#333" marker-end="url(#arr32)"/>

        <text x="430" y="42" text-anchor="middle" font-size="10.5" fill="#333">콜라이더</text>
        <circle cx="390" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="390" y="74" text-anchor="middle" font-size="10">A</text>
        <circle cx="430" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="430" y="74" text-anchor="middle" font-size="10">C</text>
        <circle cx="470" cy="70" r="14" fill="#fff" stroke="#1e4d6b"/><text x="470" y="74" text-anchor="middle" font-size="10">B</text>
        <line x1="404" y1="70" x2="416" y2="70" stroke="#333" marker-end="url(#arr32)"/>
        <line x1="456" y1="70" x2="444" y2="70" stroke="#333" marker-end="url(#arr32)"/>

        <rect x="30" y="112" width="460" height="54" rx="8" fill="#f7fafc" stroke="#c8d3db"/>
        <text x="50" y="132" font-size="10" fill="#333">규칙:</text>
        <text x="86" y="132" font-size="10" fill="#333">사슬·포크는 조건화로 닫힐 수 있음</text>
        <text x="50" y="150" font-size="10" fill="#333">콜라이더는 기본 닫힘, 콜라이더(또는 자손) 조건화 시 열림</text>
        <defs><marker id="arr32" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#333"/></marker></defs>
      </svg>

      **그림 3.2A.** `dag.html`의 핵심 도식을 3.2 맥락에 맞게 축약한 그림.

:::

    ## 연구 사례: 최소임금과 고용(Card & Krueger, 1994)

      뉴저지-펜실베이니아 패스트푸드 데이터를 DiD로 분석할 때, 핵심은 “처치 더미를 넣은 회귀”가 아니라
      **시점·지역 고정효과 구조와 평행추세 가정**을 설정하는 것이다. 같은 데이터라도
      (i) 지역별 경기 충격을 공통으로 둘지, (ii) 사전 추세 차이를 허용할지에 따라 인과 해석이 달라진다.

<svg width="520" height="180" viewBox="0 0 520 180" xmlns="http://www.w3.org/2000/svg">
        <text x="260" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#1e4d6b">SCM ↔ DAG 대응</text>
        <rect x="25" y="40" width="220" height="120" rx="8" fill="#f7fafc" stroke="#9fb2c1"/>
        <text x="35" y="64" font-size="11" fill="#333">D_t = f_D(Policy_t, U_D)</text>
        <text x="35" y="86" font-size="11" fill="#333">Y_t = f_Y(D_t, Time_t, U_Y)</text>
        <text x="35" y="108" font-size="11" fill="#333">Policy_t = g(State)</text>
        <rect x="280" y="40" width="215" height="120" rx="8" fill="#f7fafc" stroke="#9fb2c1"/>
        <circle cx="330" cy="75" r="16" fill="#fff" stroke="#1e4d6b"/><text x="330" y="79" text-anchor="middle" font-size="11">정책</text>
        <circle cx="390" cy="75" r="16" fill="#fff" stroke="#1e4d6b"/><text x="390" y="79" text-anchor="middle" font-size="11">처치</text>
        <circle cx="450" cy="75" r="16" fill="#fff" stroke="#1e4d6b"/><text x="450" y="79" text-anchor="middle" font-size="11">고용</text>
        <line x1="346" y1="75" x2="374" y2="75" stroke="#333" marker-end="url(#m32)"/>
        <line x1="406" y1="75" x2="434" y2="75" stroke="#333" marker-end="url(#m32)"/>
        <circle cx="390" cy="125" r="16" fill="#fff" stroke="#6b4c9a"/><text x="390" y="129" text-anchor="middle" font-size="10">시간충격</text>
        <line x1="390" y1="109" x2="390" y2="92" stroke="#333" marker-end="url(#m32)"/>
        <line x1="403" y1="114" x2="441" y2="88" stroke="#333" marker-end="url(#m32)"/>
        <defs><marker id="m32" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><polygon points="0 0, 7 3.5, 0 7" fill="#333"/></marker></defs>
      </svg>

      **그림 3.2.** 같은 회귀식이어도 어떤 화살표를 허용하는지가 모형 설정의 핵심이다.

:::

 ## 4. 모형 설정·식별을 DAG로 보기
      **모형 설정**은 어떤 노드를 두고 어떤 방향간선을 인정하는지로, 인과 구조와 배제 가정을 한 번에 고정하는 행위이다. **식별**은 주어진 DAG(와 필요한 부가 가정)와 관측 가능한 분포만으로 \(P(Y\mid do(X))\) 등 관심 인과량이 유일히 정해지는지의 문제이다. **d-separation**, **백도어·프론트도어 기준**, IV의 그래프 표현 등은 모두 이 그래프 위에서 식별 논리를 점검하는 도구이다. DAG가 실제 DGP와 다르면 설정 오류이며, 그 위에서의 식별 결론도 신뢰하기 어렵다. 정식 이론은 Pearl(2009) 등을 참고할 수 있다.

<svg width="360" height="140" viewBox="0 0 360 140" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arr6" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
              <polygon points="0 0, 10 3, 0 6" fill="#1e4d6b"/>
            </marker>
          </defs>
          <circle cx="180" cy="42" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="180" y="49" text-anchor="middle" font-size="16" font-weight="600">U</text>
          <line x1="158" y1="62" x2="108" y2="98" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr6)"/>
          <line x1="202" y1="62" x2="252" y2="98" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr6)"/>
          <circle cx="90" cy="110" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="90" y="117" text-anchor="middle" font-size="16" font-weight="600">T</text>
          <circle cx="270" cy="110" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2"/>
          <text x="270" y="117" text-anchor="middle" font-size="16" font-weight="600">Y</text>
          <line x1="116" y1="110" x2="244" y2="110" stroke="#1e4d6b" stroke-width="2" marker-end="url(#arr6)"/>
        </svg>

        그림 6. 예: 공통 원인 \(U\)가 처치 \(T\)와 결과 \(Y\)에 동시에 영향(\(T \leftarrow U \rightarrow Y\)), \(T \rightarrow Y\). \(T\)와 \(Y\)의 단순 연관은 인과효과와 혼동하기 쉬우며, \(U\)를 통제하거나 무작위 배정 등으로 \(U\)와 \(T\)의 연관을 끊는 식별 전략이 필요하다.

:::


      실증연구에서 식별을 위한 체크포인트는 네 가지다:
      (1) 어떤 화살표를 허용/배제할지(배제 가정),
      (2) 교란·매개·콜라이더를 구분해 조건화 전략을 고를지,
      (3) 관측 불가능 교란 \(U\)를 어떻게 다룰지(설계/감도분석),
      (4) 시간/공간 의존과 정책 시행 시점을 어떻게 구조화할지.

      다음 절에서는 이렇게 설정된 구조 아래에서, 관측분포만으로 관심 인과량을 복원할 수 있는지, 즉 식별의 문제를 본격적으로 다룬다.
