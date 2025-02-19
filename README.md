# ASAP_back
ASAP 백엔드

```python
pip install -r requirements.txt
```

# 커밋 룰

**git 커밋 룰**을 이용해 **더 나은 로그 가독성, 리뷰 프로세스, 코드 유지 보수**를 하고자 한다.

## 커밋 메세지 구조

커밋 메세지는 **Head, Body, Footer**로 구성한다. 제목을 제외한 나머지는 옵션이다.

### 형식

> Head 타입 : [#이슈 번호 - ]
>
> Body
>
> Footer(옵션)

### 타입

커밋 메세지가 **어떤 의도**를 가진 메세지인지 알린다.
**태그와 제목**으로 구성되어 있고 사용법은 **태그: 제목**의 형태이다. (`: 뒤에 space 주의!`)

**ex) Feat: Infinity Scroll 추가**

#### 태그 종류들

<table style="text-align : center;">
    <th>태그</th>
    <th>의도</th>
    <th>태그</th>
    <th>의도</th>
    <tr>
        <td style="color : red">✔️ Feat</td>
        <td style="color : red">새 기능 추가</td>
        <td style="color : red">✔️ Fix</td>
        <td style="color : red">버그 수정</td>
    </tr>
    <tr>
        <td style="color : red">✔️ Design</td>
        <td style="color : red">CSS, UI 변경</td>
        <td style="color : red">✔️ Style</td>
        <td style="color : red">포맷 변경 등 코드 수정이 없는 경우</td>
    </tr>
        <tr>
        <td style="color : red">✔️ Refactor</td>
        <td style="color : red">코드 리팩토링</td>
        <td style="color : red">✔️ Comment</td>
        <td style="color : red">주석 추가</td>
    </tr>
    </tr>
        <tr>
        <td style="color : red">✔️ Docs</td>
        <td style="color : red">문서 수정</td>
        <td>Test</td>
        <td>테스트 추가, 리팩토링</td>
    </tr>   
    </tr>
    <tr>
        <td style="color : red">✔️ Rename</td>
        <td style="color : red">파일명 수정, 이동</td>
        <td style="color : red">✔️Remove</td>
        <td style="color : red">파일 삭제</td>
    </tr>
    <tr>
        <td>Chore</td>
        <td>패키지 매니저 설정</td>
        <td>!HOTFIX</td>
        <td>급한 버그 수정</td>
    </tr>
    <tr>
        <td>!BREAKING</br>
        CHANGE</td>
        <td>커다란 API 변경</td>
        <td></td>
        <td></td>
    </tr>
</table>

### HEAD

제목은 메세지의 **짧은 요약**입니다. 다음과 같은 규칙을 가진다.

1. "고침", "추가", "변경" 등 **명령조**로 시작한다. ( 영어의 경우 동사 원형 )
2. 총 글자는 **50자** 이내
3. 마지막에 **특수문자 삽입 X**
4. **개조식** 구문 ( 간결, 요점적인 서술 )

### BODY

본문은 다음과 같은 규칙을 가진다.

1. 한 줄 당 **72자 내외**
2. **최대한 상세히 작성**
3. 어떻게보단 **무엇, 왜**에 중점적으로 작성한다.

### FOOTER

1. **이슈 트래커 ID**를 작성한다. `"유형: #이슈 번호"`

> Feat: 추가 Infinity Scroll 기능
>
> - react-intersection-observer 패키지 사용
> - intersection 관측 시 다음 page API 호출
>
> Reslves: #321
