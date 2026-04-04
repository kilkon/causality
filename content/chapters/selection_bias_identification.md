---
title: 모형 식별과 선택편향
description: 모형 식별(model identification)을 어렵게 하는 대표적인 상황이 선택편향이 발생한 경우다. 선택편향은 계량경제학에서 흔히 내생성(endogeneity)의 문제로 다루어져왔다. 내생성이 발생하면 추정된 회귀계수가 불편성을 만족하족하지 못해 모형 식별이 되지 못하는 문제가 발생한다. 
---

# 모형 식별과 선택편향

모형식별과 관련해서 널리 읽혀지는 논문은 다음과 같다. 이하의 논의는 이 세 논문을 바당으로 제기하고자 한다. 
        - **Elwert &amp; , Winship (2014)**, *Annual Review of Sociology* — 내생적 선택편향(endogenous selection bias)을 충돌변수에 대한 조건화로 통합하여 설명하고, 비모수적 식별 문제를 과잉통제·교란·내생적 선택의 세 범주로 정리한다. (편향의 *부호·크기*를 다루는 후속 방법론은 [보충: 충돌변수 편향의 방향·크기](collider_bias_magnitude_direction.html) 참고.)

        - **Holland (1986)**, *Journal of the American Statistical Association* — 통계적 연관 추론과 인과 추론의 구분, 잠재결과 관점에서의 인과효과와 “근본적 불가능성”(한 단위는 한 번에 한 처치 수준만 관찰)을 제시한다.

        - **Imbens &amp , Wooldridge (2009)**, *Journal of Economic Literature* . Recent developments in the econometrics of program evaluation. Journal of Economic Literature, 47(1), 5–86. — 프로그램 평가의 계량경제학: 자기선택·내생성, 관측 가능한 공변량에 의한 선택(selection on observables)과 그 밖의 식별 전략의 개관을 제공한다.

      ## 2. 식별의 전제: 연관과 인과, 배정 메커니즘
      Holland(1986)에 따르면, 인과효과는 단위별 잠재결과 간 대비로 정의되나 한 단위에서 실현되는 결과는 하나뿐이어서(동전의 양면을 동시에 볼 수 없음) **관찰된 연관만으로는 인과를 읽어내기 어렵다**. 식별이란 이상적인 자료에서 비인과 성분을 걸러 내어 관심 인과량을 복원할 수 있는지에 대한 분석이다(Elwert &amp; Winship 2014와 동일한 취지).

      Imbens &amp; Wooldridge(2009)는 정책·프로그램 평가에서 **참가 여부가 잠재 결과와 연관**될 때 단순한 처치군·비처치군 비교가 왜곡될 수 있음을 강조한다. 관측 공변량을 맞춘 뒤에도 편향이 남는 경우는 통상 “관측 불가능한 요인에 의한 선택” 문제로 이어지며, 도구변수·준실험·부분식별 등이 논의된다. 이는 표본 추출 자체의 문제가 아니라 **처치 배정 메커니즘**과 잠재 결과의 의존 구조 문제이기도 하다.

      ## 3. 연관의 세 근원과 세 가지 기본 구형(DAG)
      Elwert &amp; Winship(2014)은 Pearl(2009) 등의 DAG 틀을 따라, (이상적 자료에서) 비모수적 식별을 가로막는 왜곡을 세 가지로 나눈다: **과잉통제 편향(overcontrol)**, **공통원인 교란(confounding)**, **내생적 선택 편향(endogenous selection)**. 동시에, 모든 연관의 국소 구조는 다음 **세 가지 기본 구형**의 조합으로 분해된다(Pearl 1988, 2009; Verma &amp; Pearl 1988 인용).

<table>
        <thead>
          <tr>
            <th>기본 구형</th>
            <th>그래프 패턴</th>
            <th>식별상 의미(요지)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>사슬(chain)</strong></td>
            <td>\(A \rightarrow B\), \(A \rightarrow C \rightarrow B\) 등</td>
            <td>인과 경로; 중간변수 \(C\)에 <em>부당하게</em> 조건을 걸면 과잉통제로 인과효과 전달이 차단될 수 있음.</td>
          </tr>
          <tr>
            <td><strong>갈래(fork)</strong></td>
            <td>\(A \leftarrow C \rightarrow B\)</td>
            <td>공통 원인 \(C\)로 인한 비인과 연관; \(C\)를 적절히 조건화하면 차단(교란 보정).</td>
          </tr>
          <tr>
            <td><strong>역갈래(inverted fork)</strong></td>
            <td>\(A \rightarrow C \leftarrow B\)</td>
            <td>\(C\)는 충돌변수; 주변적으로는 \(A,B\)가 독립일 수 있으나 <strong>\(C\) 또는 그 자손에 조건</strong>을 걸면 비인과 경로가 열림(내생적 선택).</td>
          </tr>
        </tbody>
      </table>

      Elwert &amp; Winship(2014)의 정리: **교란**은 통제하지 말아야 할 공통 결과가 아니라 통제해야 할 공통 원인에서 오고, **내생적 선택**은 통제하면 안 되는 공통 결과(충돌변수)에 조건을 걸 때 발생하며, **과잉통제**는 인과 경로 위의 변수에 조건을 걸어 발생한다.

      ## 4. 사슬(chain)과 과잉통제 편향
      \(A\)가 \(C\)를 거쳐 \(B\)에 영향을 줄 때, 주변 연관은 총인과효과를 반영할 수 있다. 그러나 회귀에서 \(C\)를 통제하면 \(A \rightarrow C \rightarrow B\) 경로가 끊겨, 조건부 연관이 총효과와 어긋날 수 있다(Elwert &amp; Winship 2014, Figure 2).

<figure>
          <svg width="560" height="250" viewBox="0 0 560 250" xmlns="http://www.w3.org/2000/svg" aria-labelledby="cap-chain">
            <title id="cap-chain">사슬 구조와 중간변수 조건화</title>
            <defs>
              <marker id="m1" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker>
            </defs>
            <text x="12" y="24" font-size="14" fill="#4a4a4a">(가) 인과 사슬 — 주변 연관이 총효과에 해당</text>
            <circle cx="80" cy="110" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="80" y="118" text-anchor="middle" font-size="17" font-weight="600">A</text>
            <line x1="108" y1="110" x2="214" y2="110" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m1)"/>
            <circle cx="250" cy="110" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="250" y="118" text-anchor="middle" font-size="17" font-weight="600">C</text>
            <line x1="278" y1="110" x2="384" y2="110" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m1)"/>
            <circle cx="420" cy="110" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="420" y="118" text-anchor="middle" font-size="17" font-weight="600">B</text>
            <text x="12" y="178" font-size="14" fill="#4a4a4a">(나) C에 조건(박스) — 인과 경로 차단, 과잉통제</text>
            <rect x="218" y="188" width="64" height="58" rx="8" fill="rgba(30,77,107,0.12)" stroke="#1e4d6b" stroke-width="1.5" stroke-dasharray="4 2"/>
            <circle cx="80" cy="217" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="80" y="225" text-anchor="middle" font-size="17" font-weight="600">A</text>
            <line x1="108" y1="217" x2="218" y2="217" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m1)"/>
            <circle cx="250" cy="217" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="250" y="225" text-anchor="middle" font-size="17" font-weight="600">C</text>
            <line x1="278" y1="217" x2="384" y2="217" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m1)"/>
            <circle cx="420" cy="217" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="420" y="225" text-anchor="middle" font-size="17" font-weight="600">B</text>
          </svg>
          <figcaption>그림 1. 사슬 \(A \rightarrow C \rightarrow B\). (나)에서 점선 박스는 Elwert &amp; Winship(2014)이 쓰는 “조건화” 표시에 대응한다.</figcaption>
        </figure>

:::

        **행정학 예시.** \(A\)=조직의 *디지털 역량 투자*, \(C\)=*내부 절차 간소화*, \(B\)=*민원 처리 기간*이라 하자. 총효과를 보려면 간소화를 통로로 두는 것이 자연스럽다. 그런데 회귀에서 \(C\)를 통제해 “투자가 절차를 거치지 않고 기간에 직접 미치는가”만 보려 하면, 정책이 실제로 작동하는 경로를 끊어 **과잉통제**에 해당할 수 있다(연구 질문에 따라 의도적 매개 통제일 수도 있으나, 총정책효과 해석과는 별개이다).

:::

      ## 5. 갈래(fork)와 공통원인 교란
      \(A \leftarrow C \rightarrow B\)에서 주변 연관은 \(C\)를 통한 비인과 경로를 포함한다. \(C\)를 조건화하면 해당 경로가 차단되어(비모수적 가정 하) 인과량 식별에 유리해질 수 있다(Elwert &amp; Winship 2014, Figure 3).

<figure>
          <svg width="520" height="290" viewBox="0 0 520 290" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m2" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="22" font-size="14" fill="#4a4a4a">(가) 공통 원인 C — 주변 연관에 교란 혼입</text>
            <circle cx="260" cy="64" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="260" y="72" text-anchor="middle" font-size="17" font-weight="600">C</text>
            <line x1="236" y1="86" x2="118" y2="138" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m2)"/>
            <line x1="284" y1="86" x2="402" y2="138" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m2)"/>
            <circle cx="80" cy="158" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="80" y="166" text-anchor="middle" font-size="17" font-weight="600">A</text>
            <circle cx="440" cy="158" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="440" y="166" text-anchor="middle" font-size="17" font-weight="600">B</text>
            <text x="10" y="218" font-size="14" fill="#4a4a4a">(나) C에 조건화(박스) — \(A \leftarrow C \rightarrow B\) 경로 차단</text>
            <rect x="228" y="228" width="64" height="54" rx="8" fill="rgba(30,77,107,0.12)" stroke="#1e4d6b" stroke-width="1.5" stroke-dasharray="4 2"/>
            <circle cx="260" cy="255" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="260" y="263" text-anchor="middle" font-size="17" font-weight="600">C</text>
            <line x1="236" y1="244" x2="118" y2="256" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m2)"/>
            <line x1="284" y1="244" x2="402" y2="256" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m2)"/>
            <circle cx="80" cy="256" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="80" y="264" text-anchor="middle" font-size="17" font-weight="600">A</text>
            <circle cx="440" cy="256" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="440" y="264" text-anchor="middle" font-size="17" font-weight="600">B</text>
          </svg>
          <figcaption>그림 2. 포크 \(A \leftarrow C \rightarrow B\). (나)에서 점선 박스는 C에 대한 조건화이다.</figcaption>
        </figure>

:::

        **행정학 예시.** \(A\)=*규제 완화 시범 참여*, \(B\)=*지역 일자리 증가*, \(C\)=*지자체 재정·혁신 역량*이다. 역량이 높은 지자체가 시범에도 잘 들어가고 성장에도 유리하면, 참여 여부와 결과의 단순 비교는 \(C\)에 의한 **교란**을 포함한다. \(C\)를 통제하거나(또는 준실험으로 \(C\)와 \(A\)의 연관을 끊으면) Imbens &amp; Wooldridge(2009)가 말하는 관측 가능 교란 완화에 해당하는 식별 전략으로 연결된다.

:::

      ## 6. 역갈래(inverted fork)와 내생적 선택(충돌변수)
      \(A \rightarrow C \leftarrow B\)에서 \(C\)는 충돌변수이다. \(A\)와 \(B\)는 주변적으로 독립일 수 있으나, \(C\) 또는 그 **자손**에 조건을 걸면 \(A\)와 \(B\) 사이에 **가짜 연관**이 생긴다. 이것이 Elwert &amp; Winship(2014)이 말하는 **내생적 선택 편향**의 그래프적 정의이며, 표본에서 관측을 버리지 않아도 회귀 통제·층화·부분집단 분석으로 “조건화”가 일어나면 동일한 구조가 된다. 표본선택·Heckman형 선택·비응답·버크슨 편향·M-bias 등이 이 틀 아래 설명될 수 있다고 저자들은 정리한다.

<figure>
          <svg width="540" height="320" viewBox="0 0 540 320" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m3" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="24" font-size="14" fill="#4a4a4a">(가) 충돌변수 — 주변적으로 A, B 독립 가능</text>
            <circle cx="85" cy="118" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="85" y="126" text-anchor="middle" font-size="17" font-weight="600">A</text>
            <circle cx="455" cy="118" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="455" y="126" text-anchor="middle" font-size="17" font-weight="600">B</text>
            <circle cx="270" cy="44" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="270" y="52" text-anchor="middle" font-size="17" font-weight="600">C</text>
            <line x1="110" y1="100" x2="248" y2="62" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m3)"/>
            <line x1="430" y1="100" x2="292" y2="62" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m3)"/>
            <text x="10" y="168" font-size="14" fill="#4a4a4a">(나) C에 조건화 — A·B 간 비인과 연관 유도(점선)</text>
            <rect x="228" y="188" width="84" height="54" rx="8" fill="rgba(30,77,107,0.12)" stroke="#1e4d6b" stroke-width="1.5" stroke-dasharray="4 2"/>
            <circle cx="85" cy="258" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="85" y="266" text-anchor="middle" font-size="17" font-weight="600">A</text>
            <circle cx="455" cy="258" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="455" y="266" text-anchor="middle" font-size="17" font-weight="600">B</text>
            <circle cx="270" cy="232" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="270" y="240" text-anchor="middle" font-size="17" font-weight="600">C</text>
            <line x1="110" y1="244" x2="248" y2="232" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m3)"/>
            <line x1="430" y1="244" x2="292" y2="232" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m3)"/>
            <path d="M 120 258 Q 270 200 420 258" fill="none" stroke="#8b4513" stroke-width="3" stroke-dasharray="6 4"/>
          </svg>
          <figcaption>그림 3. 역갈래 \(A \rightarrow C \leftarrow B\). (나)에서 갈색 점선은 Elwert &amp; Winship(2014)이 도식한, 조건화로 유도된 스퓨리어스 연관을 나타낸다.</figcaption>
        </figure>

:::

<figure>
          <svg width="520" height="200" viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m4" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="22" font-size="14" fill="#4a4a4a">충돌변수의 자손 D에 조건화 — C에 조건화와 질적으로 동일(Elwert &amp; Winship 2014, Figure 4c)</text>
            <circle cx="85" cy="118" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="85" y="126" text-anchor="middle" font-size="17" font-weight="600">A</text>
            <circle cx="435" cy="118" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="435" y="126" text-anchor="middle" font-size="17" font-weight="600">B</text>
            <circle cx="260" cy="58" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="260" y="66" text-anchor="middle" font-size="17" font-weight="600">C</text>
            <line x1="110" y1="98" x2="236" y2="72" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m4)"/>
            <line x1="410" y1="98" x2="284" y2="72" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m4)"/>
            <line x1="260" y1="86" x2="260" y2="132" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m4)"/>
            <rect x="218" y="132" width="84" height="48" rx="8" fill="rgba(30,77,107,0.12)" stroke="#1e4d6b" stroke-width="1.5" stroke-dasharray="4 2"/>
            <text x="260" y="162" text-anchor="middle" font-size="17" font-weight="600">D</text>
          </svg>
          <figcaption>그림 4. \(C\)의 자손 \(D\)에 조건화한 경우.</figcaption>
        </figure>

:::

        **행정학 예시(충돌변수).** 논문의 할리우드 예시(재능·미모·성공)에 대응하여, *정책 분석 역량 \(A\)*, *이해관계자 협력 \(B\)*, *중앙부처 우수사례 선정 \(C\)*를 가정한다. \(A,B\)가 주변적으로 무관해도, “우수사례에 선정된 프로그램”만 분석하면 \(C\)에 조건화하여 \(A\)와 \(B\) 사이에 **인과가 아닌 연관**이 생길 수 있다. 또한 *감사·민원 DB에만 올라온 사건*만 보면, “기록에 남음”이 \(C\)의 대리(자손 \(D\))가 되어 동일한 **내생적 선택** 문제가 된다.

:::

        **행정학 예시(Heckman형 표본선택과의 연결).** Elwert &amp; Winship(2014)은 저소득자만 임금을 본다든가(결과에 따른 절단), 취업 여성만 임금 방정식을 추정하는 고전 예를 내생적 선택의 사례로 묶는다. 이에 대응하여, *공직 재직자만* 임금·만족도를 분석하거나, *긍정적 성과가 입증된 사업*만 사후평가 데이터가 남는 경우, 선택이 잠재 결과·교란과 연관되면 동일한 식별 과제가 발생한다. 그래프는 사례마다 다르게 그려야 하며, 실제 연구에서는 DAG를 명시해 조건화·표본 정의를 점검해야 한다.

:::

      ## 7. Elwert &amp; Winship(2014) §5·§5 후반: 내생적 선택 사례와 처치 전 통제(그림 5–13)
      논문은 충돌변수가 **처치·결과와 시간적으로 어디에 놓이는지**에 따라 사회학 연구 사례를 묶는다. 아래는 원문의 표기(변수 기호·Figure 번호)를 유지한 요약이며, 각 유형은 §6의 역갈래·자손 조건화와 동일한 그래프 논리로 통일된다.

      ### 7.1 결과 이후(또는 결과의 영향을 받는 변수)에 해당하는 충돌변수
      **일반 논지.** 처치 \(T\)가 결과 \(Y\)에 인과효과가 있으면 \(T \rightarrow Y \leftarrow U\)에서 \(Y\)는 \(T\)와 오차항 \(U\) 사이의 충돌변수가 된다. 따라서 결과에 직접 절단하거나, 결과에 의해 영향을 받는 변수(응답 여부 등)에 조건을 걸면 내생적 선택이 생길 수 있다.

<table>
        <thead>
          <tr>
            <th>유형·Figure</th>
            <th>구조(요지)</th>
            <th>논문 예시</th>
            <th>행정·정책 맥락의 대응</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>표본 절단<br /><small>Figure 5</small></td>
            <td>\(E \rightarrow I \leftarrow U\). 소득 \(I\)가 충돌변수인데 저소득만 남김.</td>
            <td>Hausman &amp; Wise(1977): 교육 \(E\)가 소득에 미치는 효과를, 빈곤선 부근으로 잘라낸 표본에서 추정하면 \(E\)와 \(U\) 사이에 가짜 연관이 생긴다.</td>
            <td>특정 소득·자격 기준으로만 “관측 단위”를 남기면, 기준이 결과(또는 그 대리)와 연동될 때 동일한 절단 구조가 된다.</td>
          </tr>
          <tr>
            <td>비응답<br /><small>Figure 6</small></td>
            <td>\(I \rightarrow R \leftarrow P\). 응답 \(R\)이 충돌변수.</td>
            <td>Lin et al.(1999) 맥락: 이혼 아버지의 소득 \(I\)와 자녀 양육비 \(P\)가 응답에 영향; 완료 설문만 분석(listwise deletion)은 \(R\)에 조건화.</td>
            <td>만족도·이해관계가 응답과 양쪽 변수에 동시에 작용하면, 응답자만 남긴 분석이 처치–결과 연관을 왜곡할 수 있다.</td>
          </tr>
          <tr>
            <td>확정편향<br /><small>Figure 7, Table 1</small></td>
            <td>\(B \rightarrow S \leftarrow R\). 표본포함 \(S\)가 충돌변수.</td>
            <td>Schmutz(2005) 등: “Rolling Stone 500” 포함 \(R\)과 빌보드 1위 \(B\)가 모두 \(S\)에 강하게 영향; 성공 위주로 표본을 고르면 \(B\)–\(R\) 연관의 부호가 뒤집힐 수 있다고 논의.</td>
            <td>수상·우수사례·상위 실적만 모은 비교는 “성공에 의한 표본확정”에 가깝다. 역학 설계(케이스–대조에서 처치·결과 동시에 따른 표집 금지 등)와 연결된다.</td>
          </tr>
          <tr>
            <td>Heckman형 선택<br /><small>Figure 8</small></td>
            <td>고용 \(E\)가 \(M \rightarrow W_R \rightarrow E \leftarrow W_O\)에서 충돌변수. \(W_O\)만 취업자에게 관측.</td>
            <td>모성 \(M\), 예약임금 \(W_R\), 임금제안 \(W_O\), 취업 \(E\). 취업자만 보면 \(E\)에 조건화하여 \(M\)–\(W_O\) 간 비인과 경로가 열린다. \(M \rightarrow W_O\)가 있으면 \(W_O\)가 충돌변수의 역할도 하여(오차 \(\varepsilon\)과의 구조) 예약임금을 통제해도 일부 편향이 남을 수 있다고 설명한다.</td>
            <td>재직자·참여자·“데이터가 남은” 단위만 결과 방정식을 추정하는 관행은 사례별 DAG로 점검해야 한다.</td>
          </tr>
        </tbody>
      </table>

<figure>
          <svg width="760" height="240" viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m5" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="22" font-size="14" fill="#4a4a4a">(좌) Figure 5 절단: E→I←U &nbsp;&nbsp; (우) Figure 6 비응답: I→R←P</text>
            <circle cx="95" cy="145" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="95" y="153" text-anchor="middle" font-size="17" font-weight="600">E</text>
            <circle cx="280" cy="85" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="280" y="93" text-anchor="middle" font-size="17" font-weight="600">I</text>
            <circle cx="465" cy="145" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="465" y="153" text-anchor="middle" font-size="17" font-weight="600">U</text>
            <line x1="121" y1="132" x2="256" y2="98" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m5)"/>
            <line x1="439" y1="132" x2="304" y2="98" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m5)"/>
            <circle cx="575" cy="145" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="575" y="153" text-anchor="middle" font-size="17" font-weight="600">I</text>
            <circle cx="705" cy="85" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="705" y="92" text-anchor="middle" font-size="16" font-weight="600">R</text>
            <circle cx="705" cy="205" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="705" y="212" text-anchor="middle" font-size="16" font-weight="600">P</text>
            <line x1="601" y1="136" x2="683" y2="104" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m5)"/>
            <line x1="705" y1="179" x2="705" y2="115" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m5)"/>
          </svg>
          <figcaption>그림 5–6에 대응하는 DAG 스케치(원문 Figure 5, 6).</figcaption>
        </figure>

:::

<figure>
          <svg width="560" height="200" viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m6" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="24" font-size="14" fill="#4a4a4a">Figure 7 확정편향: B(상업적 성공)→S(표본포함)←R(비평적 성공)</text>
            <circle cx="100" cy="130" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="100" y="138" text-anchor="middle" font-size="17" font-weight="600">B</text>
            <circle cx="280" cy="62" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="280" y="70" text-anchor="middle" font-size="17" font-weight="600">S</text>
            <circle cx="460" cy="130" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="460" y="138" text-anchor="middle" font-size="17" font-weight="600">R</text>
            <line x1="126" y1="114" x2="256" y2="78" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m6)"/>
            <line x1="434" y1="114" x2="304" y2="78" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m6)"/>
          </svg>
          <figcaption>그림 7. 성공에 따른 표본확정(ascertainment)으로 \(S\)에 조건화할 때의 충돌변수.</figcaption>
        </figure>

:::

<figure>
          <svg width="620" height="230" viewBox="0 0 620 230" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m7" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="22" font-size="14" fill="#4a4a4a">Figure 8 Heckman 예시(요약): M, WR, E, WO</text>
            <circle cx="85" cy="165" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="85" y="173" text-anchor="middle" font-size="17" font-weight="600">M</text>
            <circle cx="235" cy="165" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="235" y="173" text-anchor="middle" font-size="16" font-weight="600">WR</text>
            <circle cx="385" cy="88" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="385" y="96" text-anchor="middle" font-size="17" font-weight="600">E</text>
            <circle cx="535" cy="165" r="28" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="535" y="173" text-anchor="middle" font-size="17" font-weight="600">WO</text>
            <line x1="113" y1="165" x2="207" y2="165" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m7)"/>
            <line x1="256" y1="150" x2="362" y2="108" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m7)"/>
            <line x1="507" y1="150" x2="408" y2="108" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m7)"/>
          </svg>
          <figcaption>그림 8. \(W_R \rightarrow E \leftarrow W_O\)에서 \(E\)가 충돌변수; 취업자만 분석하면 \(M\)과 \(W_O\) 사이 비인과 경로가 열릴 수 있다(원문은 \(M \rightarrow W_O\) 유무에 따라 이중 문제를 구분).</figcaption>
        </figure>

:::

      ### 7.2 처치와 결과 *사이*의 변수(중간변수·중간 시점)에 조건화
      논문은 중간변수 조건화를 “충돌변수에 대한 조건화”로 재서술한다. 종속적 절단·이탈, 학력 통제용 시험점수, 매개변수 통제가 대표적이다.

<table>
        <thead>
          <tr>
            <th>유형·Figure</th>
            <th>구조(요지)</th>
            <th>논문 예시</th>
            <th>행정·정책 맥락의 대응</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>정보성 절단·이탈<br /><small>Figure 9a–c</small></td>
            <td>(c)만 \(P \rightarrow C \leftarrow U \rightarrow D\)에서 \(C\)가 충돌변수.</td>
            <td>빈곤 \(P\)가 이혼 \(D\)에 미치는 효과를 패널에서 볼 때, 이탈 \(C\)가 \(P\)와 \(D\)의 공통 원인 \(U\)(예: 부부 갈등)에 동시에 연결되면 완전 추적 분석만으로도 편향.</td>
            <td>이탈 자체의 규모보다, 이탈이 <strong>처치·결과와 공유되는 비관측 요인</strong>과 연결되는지가 식별상 핵심이다.</td>
          </tr>
          <tr>
            <td>대리통제·시험점수<br /><small>Figure 10b–d</small></td>
            <td>(c) \(S \rightarrow Q \leftarrow U \rightarrow W\): \(Q\)가 충돌변수. (d)는 \(Q \rightarrow W\)로 과잉통제.</td>
            <td>학력 \(S\)와 임금 \(W\)의 능력 교란을 막으려 점수 \(Q\)를 넣되, \(Q\)가 교육 이후에 측정되면 \(S \rightarrow Q\)로 충돌변수가 된다. 잔여 교란 완화·내생적 선택·과잉통제가 동시에 얽힌다고 정리한다.</td>
            <td>“사후에 측정된 역량 지표”를 통제할 때, 교란 완화와 충돌변수 개방이 동시에 일어날 수 있음을 그래프로 분리해 논의해야 한다.</td>
          </tr>
          <tr>
            <td>매개·직접효과<br /><small>Figure 11a–b</small></td>
            <td>\(T \rightarrow M \leftarrow U \rightarrow Y\): \(M\)에 조건화 시 비인과 경로.</td>
            <td>Project STAR: 1학년 학급규모 \(T\), 3학년 성취 \(M\), 고교 졸업 \(Y\). \(M\)과 \(Y\)의 공통 원인 \(U\)가 있으면, \(M\)을 통제한 “직접효과” 추정은 내생적 선택에 취약. \(M \rightarrow Y\)가 없어도 \(T\)와 \(Y\)의 조건부 연관이 총효과와 달라져 가짜 간접효과로 오인될 수 있다고 설명한다.</td>
            <td>중간 성과·중간 점검 변수를 넣어 “직접 효과만” 보려는 정책 평가는, 매개와 결과의 공통 교란이 있으면 동일한 함정이 된다.</td>
          </tr>
        </tbody>
      </table>

<figure>
          <svg width="640" height="190" viewBox="0 0 640 190" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m8" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="24" font-size="14" fill="#4a4a4a">Figure 9(c): P(빈곤)→C(이탈)←U→D(이혼)</text>
            <circle cx="95" cy="118" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="95" y="126" text-anchor="middle" font-size="16" font-weight="600">P</text>
            <circle cx="310" cy="58" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="310" y="66" text-anchor="middle" font-size="16" font-weight="600">C</text>
            <circle cx="310" cy="142" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="310" y="149" text-anchor="middle" font-size="15" font-weight="600">U</text>
            <circle cx="525" cy="118" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="525" y="126" text-anchor="middle" font-size="16" font-weight="600">D</text>
            <line x1="119" y1="104" x2="288" y2="72" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m8)"/>
            <line x1="310" y1="118" x2="310" y2="84" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m8)"/>
            <line x1="334" y1="130" x2="501" y2="118" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m8)"/>
          </svg>
          <figcaption>그림 9(c). (a)(b)는 이탈이 \(P\)–\(D\) 사이 비인과 경로를 열지 않는다고 설명하고, 문제되는 것은 (c)의 공통원인 구조이다.</figcaption>
        </figure>

:::

<figure>
          <svg width="640" height="180" viewBox="0 0 640 180" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m9" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="24" font-size="14" fill="#4a4a4a">Figure 10(c): S→Q←U→W</text>
            <circle cx="90" cy="112" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="90" y="120" text-anchor="middle" font-size="16" font-weight="600">S</text>
            <circle cx="310" cy="52" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="310" y="60" text-anchor="middle" font-size="16" font-weight="600">Q</text>
            <circle cx="310" cy="132" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="310" y="139" text-anchor="middle" font-size="15" font-weight="600">U</text>
            <circle cx="530" cy="112" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="530" y="120" text-anchor="middle" font-size="16" font-weight="600">W</text>
            <line x1="114" y1="96" x2="288" y2="66" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m9)"/>
            <line x1="310" y1="106" x2="310" y2="78" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m9)"/>
            <line x1="334" y1="120" x2="506" y2="112" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m9)"/>
          </svg>
          <figcaption>그림 10(c). \(Q\)를 사전에 측정하면 (b)형으로 가정할 여지가 커진다는 논문 각주와 연결된다.</figcaption>
        </figure>

:::

<figure>
          <svg width="640" height="180" viewBox="0 0 640 180" xmlns="http://www.w3.org/2000/svg">
            <defs><marker id="m10" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker></defs>
            <text x="10" y="24" font-size="14" fill="#4a4a4a">Figure 11: T→M←U→Y</text>
            <circle cx="90" cy="112" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="90" y="120" text-anchor="middle" font-size="16" font-weight="600">T</text>
            <circle cx="310" cy="52" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="310" y="60" text-anchor="middle" font-size="16" font-weight="600">M</text>
            <circle cx="310" cy="132" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="310" y="139" text-anchor="middle" font-size="15" font-weight="600">U</text>
            <circle cx="530" cy="112" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="530" y="120" text-anchor="middle" font-size="16" font-weight="600">Y</text>
            <line x1="114" y1="96" x2="288" y2="66" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m10)"/>
            <line x1="310" y1="106" x2="310" y2="78" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m10)"/>
            <line x1="334" y1="120" x2="506" y2="112" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m10)"/>
          </svg>
          <figcaption>그림 11. 매개변수 \(M\) 통제가 충돌변수 조건화가 되는 구조(직접·간접효과의 나이브 비교에 대한 경고).</figcaption>
        </figure>

:::

      ### 7.3 처치 *이전* 충돌변수에 조건화
      **잠재 동질성(homophily)과 네트워크.** Elwert &amp; Winship(2014)은 Shalizi &amp; Thomas(2011)를 인용해, 사회관계망에서 동조·확산으로 보이는 연관이 실제 *인간관 인과(피어 효과)*가 아니라 *잠재 동질성에 따른 표본 선별*에서 올 수 있음을 내생적 선택으로 정리한다. [동질성 편향(homophily bias)의 개념·식별 전략](homophily_bias.html)은 별도 보충 문서에서 정리한다. 아래 그림은 원문 **Figure 12**의 변수·화살표 관계를 옮긴 것이며, 갈색 점선은 “\(F_{i,j}\)에 조건화했을 때 열리는 비인과 경로”를 시각적으로 강조한 것이다(원문 도식과 동일한 DAG 정보; 배치만 읽기 쉽게 조정).

<figure>
          <svg width="780" height="380" viewBox="0 0 780 380" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <marker id="m12" markerWidth="14" markerHeight="14" refX="11" refY="4" orient="auto"><polygon points="0 0, 14 4, 0 8" fill="#1e4d6b"/></marker>
            </defs>
            <text x="12" y="26" font-size="14" font-weight="600" fill="#1a1a1a">Figure 12 (Elwert &amp; Winship 2014 재구성)</text>
            <text x="12" y="46" font-size="12.5" fill="#4a4a4a">잠재 동질성으로 인한 내생적 선택 — 시민참여 \(Y\), 이타심 \(U\), 친구관계 \(F_{i,j}\)</text>
            <text x="520" y="72" font-size="12" fill="#4a4a4a">개체 \(j\)</text>
            <text x="520" y="288" font-size="12" fill="#4a4a4a">개체 \(i\)</text>
            <!-- j row: Uj, Yj(t), Yj(t+1) -->
            <circle cx="110" cy="88" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="110" y="95" text-anchor="middle" font-size="15" font-weight="600">Uj</text>
            <circle cx="280" cy="88" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="280" y="93" text-anchor="middle" font-size="13" font-weight="600">Yj(t)</text>
            <circle cx="450" cy="88" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="450" y="93" text-anchor="middle" font-size="12" font-weight="600">Yj(t+1)</text>
            <line x1="134" y1="88" x2="256" y2="88" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m12)"/>
            <path d="M 134 88 Q 300 42 426 88" fill="none" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m12)"/>
            <!-- i row: Ui, Yi(t), Yi(t+1) -->
            <circle cx="110" cy="288" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="110" y="295" text-anchor="middle" font-size="15" font-weight="600">Ui</text>
            <circle cx="280" cy="288" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="280" y="293" text-anchor="middle" font-size="13" font-weight="600">Yi(t)</text>
            <circle cx="450" cy="288" r="24" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.5"/><text x="450" y="293" text-anchor="middle" font-size="12" font-weight="600">Yi(t+1)</text>
            <line x1="134" y1="288" x2="256" y2="288" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m12)"/>
            <path d="M 134 288 Q 300 334 426 288" fill="none" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m12)"/>
            <!-- collider F -->
            <circle cx="360" cy="188" r="28" fill="#fff8f0" stroke="#1e4d6b" stroke-width="2.8"/><text x="360" y="196" text-anchor="middle" font-size="16" font-weight="600">Fi,j</text>
            <line x1="128" y1="270" x2="338" y2="208" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m12)"/>
            <line x1="128" y1="106" x2="338" y2="168" stroke="#1e4d6b" stroke-width="3" marker-end="url(#m12)"/>
            <!-- spurious path when conditioning on F: Yi(t) <- Ui -> F <- Uj -> Yj(t+1) -->
            <path d="M 256 288 L 110 288 L 360 188 L 110 88 L 426 88" fill="none" stroke="#a0522d" stroke-width="2.8" stroke-dasharray="10 6" stroke-linejoin="round"/>
            <text x="12" y="352" font-size="12" fill="#a0522d">갈색 점선: \(F_{i,j}\)에 조건화 시 열리는 비인과 경로 \(Y_i(t)\leftarrow U_i\rightarrow F_{i,j}\leftarrow U_j\rightarrow Y_j(t+1)\)</text>
          </svg>
          <figcaption><strong>그림 12.</strong> 원문 캡션 요지: 사회관계망 분석에서 잠재 동질성 때문에 생기는 내생적 선택(Elwert &amp; Winship 2014, Figure 12). \(i,j\)는 한 쌍의 개체(dyad), \(Y\)는 시민참여, \(U\)는 이타심 등 잠재 특성, \(F_{i,j}\)는 친구관계. 위쪽 행은 개체 \(j\)의 \(t\), \(t+1\) 시점 참여, 아래쪽은 개체 \(i\)의 동일 시점. 청색 화살표는 저자들이 전제로 두는 인과: 각자의 \(U\)가 자신의 \(Y\)에 작용하고, 동질성으로 \(U_i\)와 \(U_j\)가 함께 \(F_{i,j}\)를 형성한다(\(U_i \rightarrow F_{i,j} \leftarrow U_j\)). <strong>설명을 위해 \(Y_i(t)\rightarrow Y_j(t+1)\) 직접 전염은 두지 않는다.</strong> 그럼에도 친구 쌍만 분석하면 \(F_{i,j}=1\)에 조건화하여 점선 경로가 열리고, \(Y_i(t)\)와 \(Y_j(t+1)\) 사이에 연관이 생길 수 있다.</figcaption>
        </figure>

:::

      **그림을 따라 읽기.** 연구 질문은 “\(i\)의 \(t\) 시점 시민참여 \(Y_i(t)\)가 \(j\)의 \(t+1\) 시점 참여 \(Y_j(t+1)\)에 인과적으로 영향을 주는가”에 해당한다. 그림에서 \(Y_i(t)\)와 \(Y_j(t+1)\)를 잇는 *직접* 인과화살표는 없으므로, 인과적으로는 두 시점 참여가 링크되지 않는다. 그러나 친구인 다동만 남기는 분석은 관계 존재 자체에 조건을 거는 것과 같아 \(F_{i,j}\)가 충돌변수 역할을 한다. 그 결과 논문이 쓰는 비인과 경로 \(Y_i(t)\leftarrow U_i\rightarrow F_{i,j}\leftarrow U_j\rightarrow Y_j(t+1)\)가 활성화되어, 전염이 없어도 두 변수의 표본 연관이 0이 아닐 수 있다.

      **일반화.** 원문은 정리한다: 한 사람의 “처치에 가까운 변수”와 다른 사람의 “결과에 가까운 변수”에 각각 연결되지만 서로 다른 잠재 요인이, 관계 맺음·해체에 동시에 작용하면 네트워크에서 인간관 효과를 찾는 분석이 동일한 유형의 내생적 선택을 유발할 수 있다. 한 완화책으로 관계 형성(및 해체)을 명시적으로 모형화하거나(Shalizi &amp; Thomas 2011), 그림의 \(U_i\) 또는 \(U_j\)를 측정·통제하는 방안을 논한다(Elwert &amp; Winship 2014 본문).

      동질성으로 맺어진 네트워크에서 **엣지가 있는 자료만** 모으는 것은 사전 충돌변수 조건화일 수 있으므로, 피어 효과·정책 확산 주장 전에 “관계 선별”과 “행동의 공통 원인”을 DAG로 분리할 필요가 있다.

        **행정학 예시(사전 충돌변수).** 협력 네트워크·파트너십이 이미 “유사한 조직 역량·정치적 친화”에 의해 선별되었다면, 네트워크에 들어간 쌍·다자만 분석하는 것은 \(F\)에 조건화에 가깝다. 정책 확산을 주장하기 전에 동질적 연결과 인과적 확산을 그래프로 분리할 필요가 있다.

:::

      ### 7.4 어떤 처치 전(pre-treatment) 변수를 통제해야 하는가?
      Elwert &amp; Winship(2014)은 §5 후반에서, **“처치보다 앞선 시점의 변수이므로 통제한다”는 상식만으로는 부족하다**고 강조한다. 사전 변수 가운데 **사전 충돌변수**에 해당하는 것을 통제하면 오히려 내생적 선택이 커질 수 있고, Steiner et al.(2010)의 관찰연구·실험 비교 예처럼 사전 심리 성향·어휘 점수만 통제했을 때 편향이 커진 사례도 인용한다(저자들은 이것이 사전 충돌변수 통제 때문일 수 있다고 언급).

      **Figure 13의 세 패널.** \(U_1, U_2\)가 관측되지 않을 때, (a)·(b)·(c)는 주변·조건부 연관만으로는 구분하기 어렵다는 점이 논점이다.

        - **(a)** \(X\)는 \(T\)와 \(Y\)의 **공통 원인**(\(T \leftarrow X \rightarrow Y\)). \(X\)에 조건을 걸면 비인과 경로가 막혀 \(T\)의 \(Y\)에 대한 인과효과 식별에 유리하다.

        - **(b)** \(X\)는 **사전 충돌변수**이고, \(T\)와 \(Y\) 사이 비인과 경로는 \(T \leftarrow U_2 \rightarrow X \leftarrow U_1 \rightarrow Y\)에서 \(X\)가 막고 있다. **\(X\)를 통제하면** 이 경로가 열려 내생적 선택이 생긴다. 따라서 (a)와 달리 \(X\)는 두지 않는 것이 맞다.

        - **(c)** \(X\)가 공통원인 역할을 하는 경로와 충돌변수 역할을 하는 경로에 **동시에** 관여하면, 통제하면 교란은 줄지만 충돌변수가 열리고, 통제하지 않으면 그 반대가 되어 **사전 통제만으로는 총효과를 식별할 충분한 집합이 없을 수 있다**. 이 경우 VanderWeele &amp; Shpitser(2011)의 아래 규칙이 적용되지 않으며, 이진 변수에 한해 Greenland(2003)의 휴리스틱을 짧게 언급한다.

      **실무 규칙(VanderWeele &amp; Shpitser 2011, Elwert &amp; Winship 인용).** “관측된 처치 전 변수들 가운데 어떤 조합으로 총 인과효과를 식별할 수 있다”는 이론적 가정이 성립한다면, **\(T\)나 \(Y\) 가운데 하나라도 (직접·간접으로) 원인이 되는 모든 변수를 통제하라**는 조언이 나온다. 그러면 \(T\)도 \(Y\)도 원인이 아닌 사전 충돌변수(Figure 13b의 \(X\)처럼)에는 조건을 걸지 않게 되어, 그 유형의 실수를 피하기 쉽다. 다만 이 규칙 자체도 “충분한 관측 통제 집합이 존재한다”는 선행 가정에 달려 있고, (c)처럼 그 가정이 깨지면 다른 식별 전략이 필요하다.

      **결론.** 어떤 사전 변수를 넣을지는 연관 패턴이 아니라 **데이터 생성 과정에 대한 이론(DAG)**에 따라 정해진다. \(X\)가 \(T\)·\(Y\)와 상관된다고 해서 무조건 통제 변수에 넣는 관행은 (b)에서 오히려 편향을 키울 수 있다.

<figure>
          <svg width="900" height="400" viewBox="0 0 900 400" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <marker id="m13" markerWidth="16" markerHeight="16" refX="12" refY="4.5" orient="auto"><polygon points="0 0, 16 4.5, 0 9" fill="#1e4d6b"/></marker>
            </defs>
            <text x="10" y="24" font-size="14" font-weight="600" fill="#1a1a1a">Figure 13 (Elwert &amp; Winship 2014 요약)</text>
            <text x="10" y="46" font-size="12" fill="#4a4a4a">\(U_1,U_2\) 비관측일 때 (a)(b)(c)는 관측만으로 동일해 보일 수 있으나, \(X\)에 대한 통제 여부는 DAG에 따라 정반대이다.</text>
            <!-- Panel (a) T<-X->Y — 넓은 세로 간격 -->
            <text x="115" y="108" text-anchor="middle" font-size="13" font-weight="600" fill="#1e4d6b">(a) \(X\)=교란</text>
            <circle cx="115" cy="168" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.8"/><text x="115" y="176" text-anchor="middle" font-size="16" font-weight="600">X</text>
            <circle cx="50" cy="318" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.8"/><text x="50" y="326" text-anchor="middle" font-size="16" font-weight="600">T</text>
            <circle cx="180" cy="318" r="26" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.8"/><text x="180" y="326" text-anchor="middle" font-size="16" font-weight="600">Y</text>
            <line x1="115" y1="194" x2="62" y2="294" stroke="#1e4d6b" stroke-width="3.5" marker-end="url(#m13)"/>
            <line x1="115" y1="194" x2="168" y2="294" stroke="#1e4d6b" stroke-width="3.5" marker-end="url(#m13)"/>
            <text x="115" y="368" text-anchor="middle" font-size="12" fill="#4a4a4a">\(X\) 통제 권장</text>
            <!-- Panel (b) T<-U2->X<-U1->Y -->
            <text x="450" y="108" text-anchor="middle" font-size="13" font-weight="600" fill="#1e4d6b">(b) \(X\)=사전 충돌변수</text>
            <circle cx="450" cy="168" r="26" fill="#fff8f0" stroke="#1e4d6b" stroke-width="2.8"/><text x="450" y="176" text-anchor="middle" font-size="16" font-weight="600">X</text>
            <circle cx="365" cy="318" r="22" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.8"/><text x="365" y="325" text-anchor="middle" font-size="15" font-weight="600">U2</text>
            <circle cx="535" cy="318" r="22" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.8"/><text x="535" y="325" text-anchor="middle" font-size="15" font-weight="600">U1</text>
            <circle cx="285" cy="318" r="22" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.8"/><text x="285" y="325" text-anchor="middle" font-size="15" font-weight="600">T</text>
            <circle cx="615" cy="318" r="22" fill="#e8f0f5" stroke="#1e4d6b" stroke-width="2.8"/><text x="615" y="325" text-anchor="middle" font-size="15" font-weight="600">Y</text>
            <line x1="347" y1="318" x2="305" y2="318" stroke="#1e4d6b" stroke-width="3.5" marker-end="url(#m13)"/>
            <line x1="375" y1="300" x2="432" y2="188" stroke="#1e4d6b" stroke-width="3.5" marker-end="url(#m13)"/>
            <line x1="525" y1="300" x2="468" y2="188" stroke="#1e4d6b" stroke-width="3.5" marker-end="url(#m13)"/>
            <line x1="555" y1="318" x2="595" y2="318" stroke="#1e4d6b" stroke-width="3.5" marker-end="url(#m13)"/>
            <text x="450" y="368" text-anchor="middle" font-size="12" fill="#4a4a4a">\(X\) 통제 금지</text>
            <!-- Panel (c) -->
            <text x="785" y="108" text-anchor="middle" font-size="13" font-weight="600" fill="#1e4d6b">(c) \(X\)=교란+충돌변수</text>
            <circle cx="785" cy="188" r="26" fill="#f5e8e8" stroke="#1e4d6b" stroke-width="2.8"/><text x="785" y="196" text-anchor="middle" font-size="16" font-weight="600">X</text>
            <text x="785" y="248" text-anchor="middle" font-size="12" fill="#4a4a4a">\(X\)가 \(T \leftarrow X\) 및</text>
            <text x="785" y="272" text-anchor="middle" font-size="12" fill="#4a4a4a">\(T \leftarrow U_2 \rightarrow X \leftarrow U_1 \rightarrow Y\)</text>
            <text x="785" y="296" text-anchor="middle" font-size="12" fill="#4a4a4a">에 동시 관여(원문 Fig.13c)</text>
            <text x="785" y="330" text-anchor="middle" font-size="12" font-weight="600" fill="#8b4513">통제만으로는 불충분</text>
          </svg>
          <figcaption><strong>그림 13.</strong> Elwert &amp; Winship(2014) Figure 13 요약. (a) \(X\)는 \(T\)와 \(Y\)의 공통 원인. (b) 비인과 경로 \(T \leftarrow U_2 \rightarrow X \leftarrow U_1 \rightarrow Y\)에서 \(X\)는 충돌변수. (c)는 원문 그림처럼 \(X\)가 여러 비인과 경로에 동시에 끼는 경우로, 사전 통제 집합만으로는 식별이 보장되지 않을 수 있음을 나타낸다. (c) 패널은 화살표 전체를 (a)(b)와 구별해 그리기 어려워 노드 \(X\)와 문장으로 대체하였다.</figcaption>
        </figure>

:::

      위 표·그림은 Elwert &amp; Winship(2014) §5 및 Figure 5–13의 구조를 압축한 것이며, 세부 가정·추가 화살표(예: Figure 8의 \(M \rightarrow W_O\), Figure 13c의 전체 DAG)는 원문과 대조할 것.

      ## 8. d-separation과 식별 점검(요약)
      Elwert &amp; Winship(2014)는 **d-separation** 규칙을 요약한다: 경로 위 **비충돌변수**를 조건화하면 연관 전달이 막히고, **충돌변수**는 조건화하지 않았을 때 막히며, 충돌변수나 그 자손을 조건화하면 열린다. 처치와 결과 사이의 **모든 비인과 경로를 차단**하면서 **인과 경로는 끊지 않는** 관측 공변량 집합이 있으면(및 필요한 가정 하) 총효과의 비모수적 식별이 가능하다는 것이 그래프적 식별의 취지이다.

      ## 9. 참고문헌(papers 폴더)

        - Elwert, F., &amp; Winship, C. (2014). Endogenous selection bias: The problem of conditioning on a collider variable. *Annual Review of Sociology*, 40, 31–53. [doi:10.1146/annurev-soc-071913-043455](https://doi.org/10.1146/annurev-soc-071913-043455)

        - Holland, P. W. (1986). Statistics and causal inference. *Journal of the American Statistical Association*, 81(396), 945–960. [doi:10.1080/01621459.1986.10478354](https://doi.org/10.1080/01621459.1986.10478354)

        - Imbens, G. W., &amp; Wooldridge, J. M. (2009). Recent developments in the econometrics of program evaluation. *Journal of Economic Literature*, 47(1), 5–86. (원고: NBER Working Paper 14251, 2008.)

      DAG 기본 구형과의 대응 및 충돌변수 논의는 Pearl(2009) 등을 인용하는 Elwert &amp; Winship(2014) 본문을 직접 대조할 것. [dag.html](dag.html)의 사슬·포크·역갈래 도식과 병행하면 좋다.

