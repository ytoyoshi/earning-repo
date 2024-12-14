const createCounter = () => {
    let count = 0;
    return function increment() {
        // 変数`count`を参照し続けている
        count = count + 1;
        console.log(count)
        return count;
    };
};
// countUpとnewCountUpはそれぞれ別のincrement関数(内側にあるのも別のcount変数)
const countUp = createCounter();
const newCountUp = createCounter();

// それぞれの状態も別となる
console.log(countUp()); // => 1
console.log(countUp()); // => 2

