## HTML이란?

`HTML(HyperText Markup Language)`은 웹페이지를 기술하기 위한 `마크업 언어`이다. 더 자세히 말하면 웹 페이지의 `내용(content)`과 `구조(structure)`를 담당하는 언어로써, HTML 태그를 통해 정보를 구조화하는 것이다.

<br>

## HTML5의 구조

- HTML5 문서는 반드시 `<!DOCTYPE html>`으로 시작하여 문서 형식(document type)을 HTML5로 지정한다.
- 실제적인 HTML document은 2행부터 시작되는데, `<html>`과 `</html>` 사이에 기술한다.
- `<head>`와 `</head>` 사이에는 document title, 외부 파일의 참조, 메타데이터의 설정 등이 위치하며 **이 정보들은 브라우저에는 표시되지 않는다.**
- 웹브라우저에 출력되는 모든 요소는 `<body>`와 `</body>`사이에 위치한다.

<br>

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Hello, World!</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>HTML 5!</P>
    </body>
</html>
```

위와 같은 코드를 작성하면, 아래와 같이 body 안에 작성된 h1태그와 p태그의 문자열이 보이게된다.
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Hello, World!</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>HTML 5!</P>
    </body>
</html>

<br>

## HTML5 기본 문법

### 요소(Element)
