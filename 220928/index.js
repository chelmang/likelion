//함수 호출
func1();

//1. 함수 선언문
function func1(){
    console.log('this is func1');
}

//2.함수 리터럴
let func2=function(){
    console.log('this is func2');
    
}
func2;

//3.function 생성자로 정의 (객체의 생성자를 호출:new 키워드 사용)
let func3 = new Function('a,b,c',`
console.log(\'this is func3\');
console.log("test");
`);
func3();

//4. 화살표 함수 (=>) 다른 언어의 람다식과 비슷함
let func4 = () => {

}

//즉시 실행함수 
let func5 = function(){
    console.log('this is function5');
}
();

//인수: 함수에 전달하는 값
//매개변수: 전달받은 값을 저장하는 변수
//반환값: 함수 실행이 종료될 때 돌려주는 값(함수 자체의 값)
function testFunc(a){
    
}