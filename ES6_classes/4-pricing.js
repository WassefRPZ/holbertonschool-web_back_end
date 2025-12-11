
import Currency from './3-currency.js';
export default class pricing{
    constructor(amount, currency){
        this.amount = amount;
        this.currency = currency;
    }
    get amount(){
        return this._amount;
    }
    set amount(value){
        if (typeof value !== "string"){
            throw new TypeError("string Error");
        }
        this._amount = value;
    }
    get currency(){
        return this._currency;
    }
    set currency(value){
        if (!(value instanceof Currency)){
            throw new TypeError("string name Error");
        }
        this._currency = value;
    }
    displayFullCurrency() {
        return `${this.amount} ${this.currency.code}(${this.currency.code})`;
    }
    static convertPrice(amount, conversionRate){
        if (typeof amount !== "number" || typeof conversionRate !== "number"){
            throw new TypeError("amount and conversionrate must be numbers");
        }
        return amount * conversionRate
    }
}
