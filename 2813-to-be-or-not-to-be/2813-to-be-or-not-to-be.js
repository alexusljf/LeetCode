/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const toBe = (val2) => {
        if (val !== val2){
            throw("Not Equal")
        }
        return true
    }
    const notToBe = (val2) => {
        if (val === val2){
            throw("Equal")
        }
        return true
    }
    return {toBe, notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */