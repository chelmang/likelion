//1번. 15부터 30까지 순서대로 출력하세요
//그리고 15부터 30까지의 합계와 평균을 출력하시오.

//평균 = 합계 / 개수
//출력결과: "15~30까지의 합계: ?? , 평균: ??"
let sum = 0; //합계가 될 변수
for(let i=15;i<=30;i++){
    console.log(i);
    sum+=i; //sum에 i를 계속 더해준다.
}
console.log(`15~30까지의 합계: ${sum}, 평균: ${sum/16}`);

//2번.3단 구구단을 출력하세요.(3x11 ~ 3x9)
//여기서 곱의 결과가 9의 배수는 제외하고 출력하세요.

for (let i = 1;i<10;i++){
    if((3*i) % 9 !==0){
    console.log(`3x ${i} = ${3*i}`);
    }
}

//명시적: 프로그래머가 직접 작성
//묵시적: 프로그램이 알아서


let i = '2'
//묵시적
console.log(i+'test');
console.log(i-0+5);
console.log(+i);
//명시적
let result = parseInt('3.14'); //정수로
console.log(result);
result=Number(10); //10
console.log(Number('10')); //10
Number(true); //1
Number("1234.567"); //1234.567 
//숫자를 문자열로
Number.toString(1532);
let n = 26
n.toString();
n.toFixed(0);//소수점 0번째자리까지 문자열

//심볼 : 유일무이한 값
let sym = Symbol();
let sym2 =Symbol();
console.log(sym == sym2); //false
let sym3 = Symbol("테스트");
console.log(sym == sym3);
console.log(sym.toString());
sym3=Symbol.for('테스트');
console.log(Symbol.keyFor(sym3))

let meassage = 'This \
is test';
meassage=`This
is test`
meassage = String.raw`This\nis test`;


let card = { 
    'rank': "A",
    price: "1500" 
};
card.rank = 'B';
card.price=3000;
card.name='푸른눈의 백룡';
console.log(card['rank']);
console.log(card['price']);

while(true){
   sdfsfsdf: while(true){
        console.log(1)
        break sdfsfsdf;
    }
    //deadcode
    console.log(1)
    break;
}

try{ //안에 있는 구문을 시도함, 시도하다가 에러 발생 시 catch 문으로 이동함
    console.log(card['price']);
    //예외처리(try - catch)
    //try안에는 처리해야할 코드 작성
    //catch에는 에러(예외)가 발생했을 경우 처리할 코드를 작성
}
catch(fdgfdgdfg){
    console('에러가 발생했습니다!');
    console.log(e);
}
finally{
    //에러가 발생하든 안하든 무조건 실행됨
}
console.log('프로그램종료');



let computer={
    'cpu':'i5',
    'ram': '15gb',
    'graphic': 'gforce-1080'
};

//pro라는 이름의 변수에 computer의 프로퍼티가 순서대로 저장되면서 실행됨
for(let pro in computer){
    //computer[pro]
    console.log(`프로퍼티:${pro}, 값: ${computer[pro]}`);
    console.log(computer[pro]);
}

let arr = [10, 20, 30, 40, 50];
for(let value of arr){
    console.log(arr);
}