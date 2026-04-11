---
title: 20.1 Rosenbaum 경계와 \(\Gamma\)-민감도
description: Rosenbaum 경계는 매칭 설계에서 관측되지 않은 교란이 처치할당 odds를 얼마나 바꿀 수 있어야 결과가 흔들리는지를 보여주는 도구다. 이 절은 \(\Gamma\)-민감도의 의미와 정책평가 해석을 자세히 설명한다.
---

# 18.1 Rosenbaum 경계와 \(\Gamma\)-민감도관측연구에서 매칭을 수행하면 “관측된 공변량 기준으로는” 처치군과 비교군을 비슷하게 만들 수 있다. 그러나 여전히 남는 질문이 있다. **관측되지 않은 교란이 있었다면 이 결론은 얼마나 쉽게 흔들릴까?** Rosenbaum 경계(bounds)는 바로 이 질문에 답한다.

## 기본 아이디어

매칭된 두 단위 \(i,j\)가 관측 공변량 \(X\)는 같지만, 관측되지 않은 요인 \(u\) 때문에 처치받을 확률이 다를 수 있다고 하자. Rosenbaum은 이 차이를 odds ratio의 비율로 제한한다.

\[
\frac{1}{\Gamma}
\le
\frac{\Pr(T_i=1\mid X_i,u_i)\Pr(T_j=0\mid X_j,u_j)}
     {\Pr(T_i=0\mid X_i,u_i)\Pr(T_j=1\mid X_j,u_j)}
\le
\Gamma
\]

여기서 \(\Gamma=1\)이면 숨은 교란이 전혀 없다는 뜻이고, \(\Gamma>1\)이면 숨은 교란이 매칭쌍 داخل에서 처치 odds를 다르게 만들 수 있음을 뜻한다.

## \(\Gamma\)는 어떻게 해석하는가

- \(\Gamma=1\): 완전한 무은닉성, 즉 숨은 교란이 없음
- \(\Gamma=1.5\): 어떤 두 매칭쌍 구성원은 관측되지 않은 요인 때문에 처치 odds가 최대 1.5배까지 다를 수 있음
- \(\Gamma=2\): 숨은 교란이 처치 odds를 최대 2배까지 차이 나게 할 수 있음

연구자는 보통 “결과의 유의성이 어느 \(\Gamma\)까지 유지되는가”를 보고한다.

## 왜 유용한가

Rosenbaum 경계는 숨은 교란의 존재 여부를 직접 검증하지는 못한다. 대신 “어느 정도 강도의 숨은 교란이 있어야 결론이 무너지는가”를 보여준다. 즉 이것은 숨은 교란의 존재를 부정하는 도구가 아니라, **결론의 취약성 임계점**을 제시하는 도구다.

## 시각적으로 보면

<figure class="chapter-figure">
  <svg viewBox="0 0 760 300" role="img" aria-labelledby="gamma-visual-title gamma-visual-desc">
    <title id="gamma-visual-title">Gamma 민감도 시각화</title>
    <desc id="gamma-visual-desc">감마가 커질수록 숨은 교란 허용 폭이 커지고, 어느 지점에서 결론 유지 구간이 끝나는지를 보여주는 도식이다.</desc>
    <rect x="0" y="0" width="760" height="300" fill="#fbfaf4"></rect>
    <line x1="90" y1="235" x2="700" y2="235" stroke="#293241" stroke-width="2"></line>
    <text x="705" y="241" font-size="16" fill="#293241">\(\Gamma\)</text>
    <line x1="130" y1="235" x2="130" y2="115" stroke="#2f5d50" stroke-width="8"></line>
    <line x1="130" y1="115" x2="470" y2="115" stroke="#2f5d50" stroke-width="8"></line>
    <circle cx="470" cy="115" r="10" fill="#2f5d50"></circle>
    <text x="118" y="260" font-size="15" fill="#293241">1.0</text>
    <text x="448" y="260" font-size="15" fill="#293241">1.8</text>
    <text x="490" y="120" font-size="15" fill="#2f5d50">이 지점까지 결론 유지</text>
    <line x1="470" y1="115" x2="640" y2="180" stroke="#c56a3b" stroke-width="6"></line>
    <text x="592" y="192" font-size="15" fill="#c56a3b">이후에는 결론 취약</text>
    <rect x="140" y="38" width="440" height="42" rx="10" fill="#eef4ea" stroke="#b7c8b2"></rect>
    <text x="158" y="64" font-size="15" fill="#2f5d50">\(\Gamma^*\)가 클수록 “꽤 강한 숨은 교란이 있어야 결론이 무너진다”는 뜻</text>
  </svg>
  <figcaption>Rosenbaum 경계는 결과의 유의성이 유지되는 최대 \(\Gamma\)를 통해 결론의 강건성을 표현한다.</figcaption>
</figure>

## 정책평가 사례

직업훈련 프로그램 평가에서 성향점수매칭을 했다고 하자. 연구자는 학력, 연령, 기초임금, 실업기간 등을 매칭했지만, 여전히 “동기” 같은 미관측 특성이 남아 있을 수 있다. 이때 Rosenbaum 경계는 “그런 숨은 요인이 처치 odds를 1.2배만 바꿔도 결론이 무너지는지, 아니면 2배 이상이어야 무너지는지”를 보여준다.

만약 \(\Gamma=1.1\)만 되어도 유의성이 사라진다면 결과는 매우 취약하다. 반대로 \(\Gamma=2.5\)까지도 유지된다면, 꽤 강한 숨은 교란이 있어야 결론이 흔들린다는 뜻으로 읽을 수 있다.

## 해석상의 주의

- \(\Gamma\)가 크다고 해서 숨은 교란이 없다는 뜻은 아니다.
- \(\Gamma\)는 odds 비율 기준이므로 직관이 완전히 쉽지는 않다.
- 연구맥락상 그 정도 교란이 현실적으로 가능한지 서술적 해석이 필요하다.
- 매칭 설계와 특히 잘 맞지만, 다른 설계에 기계적으로 일반화하면 안 된다.

## 정리

Rosenbaum 경계는 숨은 교란의 존재를 없애주는 도구가 아니라, 그 가능성 앞에서 결론이 얼마나 버티는지를 보여주는 도구다. 다음 절에서는 비슷한 질문을 좀 더 요약된 숫자로 전달하는 E-value를 살펴본다.
