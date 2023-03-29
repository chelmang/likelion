//변수-var,let,const 키워드를 사용해서 변수를 생성
//const : 상수,변수를 생성했을 때 값을 할당해야한다
//boolean: true/false(참, 거짓)
// 한줄주석
/*여러줄 주석*/ 
var v1 = 2.5;
var v1=44;
console.log(v1);

let v2=true; //변수 다시 선언 불가능
v2=4;
console.log(v2);

let meassage = 'this is test';
console.log(meassage);


let version = "ECMAScript";
let versionNumber=6;
//공백문자==띄어쓰기
console.log('C:\\Users\\Administrator'); //백슬레시 두개 써줘야 하나로 나옴
console.log('this \nis\n test' + version + versionNumber );


/***********연산자************/
//+, -, *, /, %(나머지 연산)
//5%2 -> 몫: 2, 나머지: 1
const a1=5; //const: 상수개념
const a2=2;
console.log(a1+'/'+a2+'->몫:'+ (a1/a2)+"나머지:" + (a1%a2));
console.log(`${a1}/${a2}->몫: ${a1/a2}, 나머지: ${a1%a2} `)

//변수 명명 규칙 CamelCase, PascalCase, SnakeCase
//LowerCamelCase: 단어마다 대문자, 시작은 소문자
//thisIsCamelCase
//PascalCase, UpperCamelCase: 단어마다 대문자, 시작도 대문자
//ThisIsCamelCase
//SnakeCase: 단어마다 _로 잇기 (단어마다 소문자)
//this_is_snake_case
//JS에서 권고하는 방식
//함수, 변수이름 => 카멜케이스
//클래스 => 파스칼케이스
//강사 추천
//변수 => 카멜케이스
//함수 => 스네이크케이스
//클래스 => 파스칼케이스

/***********220927*************** */
//조건문, 절 (if, switch)
//JS에서의 비교 연산
//a == b: a값이 b값과 동일한가?에 대한 결과를 반환. 단, 형변환을 할 수 있다면 형변환 후 판단
//a !=b: a값이 b값과 동일하지않은가?에 대한 결과를 반환.단, 형변환을 할 수 있다면 형변환 후 판단
//a === b : a값이 b값과 동일한가?에 개한 결과를 반환. 형변환하지 않고 그 값 그대로 판단
//a !== b: a값이 b값과 동일하지 않은가?에 대한 결과를 반환. 형변환하지 않고 그 값 그대로 판단

//true = '1'
//false = '0'
const num1 = 1;
const num2 = 1;
console.log(`num1==num2 -> ${num1 == num2}`);
console.log(`num1==num2 -> ${num1 === num2}`);

//if(조건){
//      조건이 참일 때 실행할 실행문    
//}
//if-else if - else
if(num1 < num2){
    console.log('참')
}
else if(num1===num2){
    console.log('같음')
}
else{
    console.log('거짓')
}

//&&: AND, ||: OR ,!: NOT
consol.log(num1<num2 ||num2);

//switch: 하나의 데이터 값을 다른 여러 데이터랑 비교 연산함
switch(판단하고싶은데이터){
    case 데이터와비교할값:
        break;
    default:
        break;
}

switch(num1){
    case 1:
        console.log(1);
        break;
    case 5:
        console.log(5);   
    case num2:
        console.log('num2');
    default:
        console.log('해당없음');         
}

//++, --  증감연산
// +=, -=, *=, /=, %=, |=, ??= 대입연산
//a &=b -> a&&b여부를 a에게 대입
//a |=b -> a||b 여부를 a에게 대입
//a ??= b -> a가 null이거나 undefined일 때만 b값을 a에게 대입
//증감연산 : 1(한 단계) 증가, 또는 감소시킨다 
let n1 =4;
n1+=4*2+1;
n1 ++; //n1은 5가 된다 -> n1 = n1+1; -> n1+=1;
n1--; //n1은 4가 된다 ->n1 = n1 -1; n1-=1;
--n1;

let number1 = 1;
let number2 = 1;
let result1 = number1++; //후위: 현재 명령어(연산)을 끝낸 후 증가
let result2 = ++number2; //전위: 현재 명령(연산)을 하기 전에 증가
console.log(`number1: ` + number1);
console.log(`number2: ` + number2);
console.log(`result1: ` + result1);
console.log(`result2: ` + result2);

//반복절(문)
//for- 반복횟수가 있을 때 사용하면 좋음, while-조건이 있을 때 사용하면 좋다
//while(조건){조건이 맞을 때 실행할 명령문}
let number =0;
while(number<10){
    console.log(number);
    number++;
}

//for(초기화식;조건식;증감식){조건이 true일 때 실행할 명령문}
//초기화식:변수를 생성하거나 변수에 값을 대입함
//조건식:for 반복을 언제까지 진행할지에 대한 조건식
//증감식:변수의 값을 변경하거나 증가/감소 시킴
for(a=2;a;a+=10){
    console.log('실행')
}









const v3=0x10; //-> 10진수로 16  속도빠름
