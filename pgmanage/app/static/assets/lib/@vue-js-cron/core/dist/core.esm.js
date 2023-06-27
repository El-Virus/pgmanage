import Mustache from 'mustache';

var script$1 = {
  inheritAttrs: false,
  name: 'RenderlessSelect',
  props: {
    multiple: {
      type: Boolean,
      default: false
    },
    modelValue: {
      type: [String, Array, Object],
      default (props) {
        return props.multiple ? [] : null
      }
    },
    items: {
      type: Array,
      default: () => []
    },
    returnObject: {
      type: Boolean,
      default: false
    },
    itemText: {
      type: String,
      default: 'text'
    },
    itemValue: {
      type: String,
      default: 'value'
    },
    cols: {
      type: Number,
      default: 1
    },
    selection: {
      type: String,
      default: ''
    },
    clearable: {
      type: Boolean,
      default: false
    }
  },
  emits: ['update:model-value'],
  data () {
    return {
      menu: false
    }
  },
  computed: {
    _value () {
      return (this.multiple) ? this.modelValue : [this.modelValue]
    },
    selectedItems () {
      return this.items.filter((item) => {
        for (const value of this._value) {
          if (this.returnObject) {
            if (value === item) return true
          } else {
            if (value === item[this.itemValue]) return true
          }
        }
        return false
      })
    },
    selectedStr () {
      return this.selection || this.selectedItems.map((item) => item[this.itemText]).join(',')
    },
    rows () {
      return Array.isArray(this.items) ? Math.ceil(this.items.length / this.cols) : 0
    },
    itemRows () {
      return Array.from(Array(this.rows), (_, i) => {
        return Array.from(Array(this.cols), (_, j) => {
          return this.items[this.cols * i + j]
        })
      })
    }
  },
  methods: {
    select (item) {
      if (!item) {
        return
      }

      if (this.multiple) {
        const value = this.selectedItems.slice();
        const i = this.selectedItems.indexOf(item);
        // deselect
        if (i >= 0) {
          value.splice(i, 1);
        } else { // select
          value.push(item);
        }
        this.$emit('update:model-value', (this.returnObject) ? value : value.map((item) => item[this.itemValue]));
      } else {
        this.$emit('update:model-value', (this.returnObject) ? item : item[this.itemValue]);
      }
    },
    isSelected (item) {
      return this.selectedItems.includes(item)
    },
    clear () {
      this.$emit('update:model-value', this.multiple ? [] : null);
    }
  },

  render () {
    if (!this.$slots || !this.$slots.default) {
      return
    }

    return this.$slots.default({
      selectedStr: this.selectedStr,
      modelValue: this.modelValue,
      items: this.items,
      select: this.select,
      isSelected: this.isSelected,
      clearable: this.clearable && this.selectedItems.length > 0,
      clear: this.clear,
      cols: this.cols,
      rows: this.rows,
      itemRows: this.itemRows,
      multiple: this.multiple,
      itemText: this.itemText,
      itemValue: this.itemValue
    })
  }
};

script$1.__file = "src/components/renderless-select.vue";

const CronType = {
  Empty: 'empty',
  Value: 'value',
  Range: 'range',
  EveryX: 'everyX',
  Combined: 'combined'
};

const Position = {
  Prefix: 'prefix',
  Suffix: 'suffix',
  Text: 'text'
};

class Field {
  /**
     *
     * @param {String} name
     * @param {Array} items
     */
  constructor (id, items) {
    this.id = id;
    this.items = items;

    this.itemMap = this.items.reduce((acc, item) => {
      acc[item.value] = item;
      return acc
    }, {});
  }

  get min () {
    return this.items[0].value
  }

  get max () {
    return this.items[this.items.length - 1].value
  }

  getItem (value) {
    return this.itemMap[value]
  }
}

class CronSegment {
  get type () {
    return CronType.Value
  }

  get value () {
    return '*'
  }
}

class AnySegment extends CronSegment {
  get type () {
    return CronType.Empty
  }

  get value () {
    return '*'
  }
}

class RangeSegment extends CronSegment {
  constructor (start, end) {
    super();
    this.start = start;
    this.end = end;
  }

  get type () {
    return CronType.Range
  }

  get value () {
    return `${this.start}-${this.end}`
  }
}

class EverySegment extends CronSegment {
  constructor (every) {
    super();
    this.every = every;
  }

  get type () {
    return CronType.EveryX
  }

  get value () {
    return `*/${this.every}`
  }
}

class ValueSegment extends CronSegment {
  constructor (value) {
    super();
    this.val = value;
  }

  get type () {
    return CronType.Value
  }

  get value () {
    return '' + this.val
  }
}

class CombinedSegment extends CronSegment {
  constructor (segments = []) {
    super();
    this.segments = segments;
  }

  get type () {
    return CronType.Combined
  }

  addSegment (cronSegment) {
    this.segments.push(cronSegment);
  }

  get value () {
    return this.segments.map((c) => c.value).join(',')
  }
}

function range$1 (start, end, step = 1) {
  const r = [];
  for (let i = start; i <= end; i += step) {
    r.push(i);
  }
  return r
}

class Range {
  constructor (start, end, step = 1) {
    this.start = start;
    this.end = end;
    this.step = step;

    return new Proxy(this, {
      get: function (target, prop) {
        const i = (typeof prop === 'string') ? parseInt(prop) : prop;
        if (typeof i === 'number' && i >= 0 && i <= target.length) {
          return target.start + target.step * i
        }
        return Reflect.get(...arguments)
      }
    })
  }

  get length () {
    return parseInt((this.end - this.start) / this.step) + 1
  }

  [Symbol.iterator] () {
    let index = -1;
    return {
      next: () => {
        return { value: this[++index], done: !(this[index + 1] !== undefined) }
      }
    }
  }
}

function getValue (params, key) {
  const keys = key.split('.');
  let value = params;
  for (const k of keys) {
    value = value[k];
  }
  return value
}

function format (str, params) {
  const re = /\{\{\S+\}\}/gm;
  let m;
  while ((m = re.exec(str)) !== null) {
    const key = m[0].substring(2, m[0].length - 2);
    const value = getValue(params, key);
    str = str.substr(0, m.index) + value + str.substr(m.index + m[0].length);
    re.lastIndex = m.index;
  }
  return str
}

/**
 * type definition
 * @name toText
 * @function
 * @param {number} value
 * @returns {string}
*/

/**
 * generate items for fields
 * @param {number} min first value
 * @param {number} max last value
 * @param {toText} genText returns a string representation of value
 * @param {toText} genAltText returns an alternative string representation of value
 * @returns {Array<{value:number, text:string, alt:string}>} array of items
 */
function genItems$1 (min, max, genText = (value) => { return value + '' }, genAltText = (value) => { return value + '' }) {
  const res = [];
  for (const i of new Range(min, max)) {
    const item = {};
    item.text = genText(i);
    item.alt = genAltText(i);
    item.value = i;
    res.push(item);
  }
  return res
}

/**
 * pads numbers
 * @param {number} n number to pad
 * @param {number} width
 * @example
 * //returns "001"
 * util.pad(1,3)
 * @returns {string} the padded number
 */
function pad$1 (n, width) {
  n = n + '';
  return (n.length < width) ? new Array(width - n.length).fill('0').join('') + n : n
}

/**
 * determines whether the passed value is an object
 * @param {any} value
 * @returns {Boolean} true if value is an object, otherwise false
 */
function isObject (value) {
  return (value && typeof value === 'object' && !Array.isArray(value))
}

/**
 * copies (deep copy) all properties from each source to target
 * @param {object} target
 * @param  {...object} sources
 * @returns {object} target
 */
function deepMerge (target, ...sources) {
  if (!isObject(target) || sources.length === 0) return
  const source = sources.shift();

  if (isObject(source)) {
    for (const [key, value] of Object.entries(source)) {
      if (isObject(value)) {
        if (!isObject(target[key])) {
          target[key] = {};
        }
        deepMerge(target[key], source[key]);
      } else {
        target[key] = source[key];
      }
    }
  }

  if (sources.length > 0) deepMerge(target, sources);
  return target
}

function traverse$1 (obj, ...keys) {
  if (keys.length === 0) { return obj }

  for (const key of keys[0]) {
    if (key in obj) {
      const res = traverse$1(obj[key], ...keys.slice(1));
      if (res !== undefined) {
        return res
      }
    }
  }
}

function populate (obj, map) {
  const res = {};
  for (const [key, value] of Object.entries(obj)) {
    res[key] = map[value];
  }
  return res
}

function isSquence (numbers) {
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i - 1] + 1 !== numbers[i]) {
      return false
    }
  }
  return true
}

var util = {
  range: range$1,
  Range,
  format,
  genItems: genItems$1,
  pad: pad$1,
  deepMerge,
  isObject,
  traverse: traverse$1,
  populate,
  isSquence
};

function strToArray$4 (str) {
  if (str !== '*') {
    return null
  }
  return []
}

function arrayToStr$4 (arr, field) {
  const { items } = field;

  if (arr.length === 0) {
    return new AnySegment()
  }
  if (arr.length !== items.length) {
    return null
  }

  for (const item of items) {
    if (!arr.includes(item.value)) {
      return null
    }
  }
  if (!util.isSquence(items.map(item => item.value))) {
    return null
  }
  return new AnySegment()
}

var any = {
  strToArray: strToArray$4,
  arrayToStr: arrayToStr$4
};

// */x

const re$1 = /^\*\/\d+$/;

function strToArray$3 (str, { min, max }) {
  if (!re$1.test(str)) {
    return null
  }

  const [, everyStr] = str.split('/');
  const every = parseInt(everyStr);

  const start = every * parseInt(min / every);
  const res = [];
  for (let i = start; i <= max; i += every) {
    if (i >= min) {
      res.push(i);
    }
  }
  return res.length > 0 ? res : null
}

function arrayToStr$3 (arr, field) {
  const { min, max } = field;

  if (arr.length < 3) {
    return null
  }

  const step = arr[1] - arr[0];
  if (step <= 1) {
    return null
  }

  const first = (min % step === 0) ? min : (parseInt(min / step) + 1) * step;
  if (arr.length !== parseInt((max - first) / step) + 1) {
    return null
  }

  for (const value of arr) {
    if (value % step !== 0) {
      return null
    }
  }

  return new EverySegment(step)
}

var every = {
  strToArray: strToArray$3,
  arrayToStr: arrayToStr$3
};

// x-y

const re = /^\d+-\d+$/;

function strToArray$2 (str, { min, max }) {
  if (!re.test(str)) {
    return null
  }

  const range = str.split('-');
  const start = parseInt(range[0]);
  const end = parseInt(range[1]);

  if (start > end || start < min || end > max) {
    return null
  }

  return util.range(start, end)
}

function arrayToStr$2 (arr, field) {
  const { min, max } = field;

  if (arr.length <= 1) {
    return null
  }

  const minValue = arr[0];
  const maxValue = arr[arr.length - 1];

  if (minValue < min) {
    return null
  }
  if (maxValue > max) {
    return null
  }

  const ranges = [];
  let start = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i + 1] === undefined || arr[i + 1] - arr[i] > 1) {
      if (i === start) {
        ranges.push(new ValueSegment(arr[start]));
      } else {
        ranges.push(new RangeSegment(arr[start], arr[i]));
      }
      start = i + 1;
    }
  }

  return new CombinedSegment(ranges)
}

var range = {
  strToArray: strToArray$2,
  arrayToStr: arrayToStr$2
};

// x

function strToArray$1 (str, { min, max }) {
  const number = parseInt(str);
  return (String(number) === str && number >= min && number <= max) ? [number] : null
}

function arrayToStr$1 (arr, field) {
  const { min, max } = field;

  if (Math.min(arr) < min) {
    return null
  }
  if (Math.max(arr) > max) {
    return null
  }

  const values = arr.map((x) => { return new ValueSegment(x) });
  return new CombinedSegment(values)
}

var value = {
  strToArray: strToArray$1,
  arrayToStr: arrayToStr$1
};

// x,y,z

const fieldTypes = [any, every, range, value];

function strToArray (str, field) {
  const fields = str.split(',');
  const res = [];
  for (const f of fields) {
    if (f === '*') {
      return []
    }

    let values = null;
    for (const fieldType of fieldTypes) {
      values = fieldType.strToArray(f, field);
      if (values !== null) {
        break
      }
    }
    if (values === null) {
      return null
    }
    res.push(...values);
  }
  return Array.from(new Set(res))
}

function arrayToStr (arr, field) {
  for (const fieldType of fieldTypes) {
    const value = fieldType.arrayToStr(arr, field);
    if (value) {
      return value
    }
  }
  return null
}

var multiple = {
  strToArray,
  arrayToStr
};

var cn = {
  '*': {
    prefix: '每',
    suffix: '',
    text: '未知',
    '*': {
      empty: { text: '每 {{field.id}}' },
      value: { text: '{{val.text}}' },
      range: { text: '{{start.text}}-{{end.text}}' },
      everyX: { text: '每 {{every.value}}' }
    },
    month: {
      '*': { prefix: '的' },
      empty: { text: '每月' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    day: {
      '*': { prefix: '的' },
      empty: { text: '每日' },
      value: { text: '{{val.alt}}号' },
      range: { text: '{{start.alt}}号-{{end.alt}}号' }
    },
    dayOfWeek: {
      '*': { prefix: '的' },
      empty: { text: '一周的每一天' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    hour: {
      '*': { prefix: '的' },
      empty: { text: '每小时' }
    },
    minute: {
      '*': { prefix: ':' },
      empty: { text: '每分钟' }
    }
  },
  minute: {
    text: '分'
  },
  hour: {
    text: '小时',
    minute: {
      '*': {
        prefix: ':',
        suffix: '分钟'
      },
      empty: { text: '每' }
    }
  },
  day: {
    text: '天'
  },
  week: {
    text: '周',
    dayOfWeek: {
      '*': { prefix: '的' },
      empty: { text: '每天' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    }
  },
  month: {
    text: '月',
    dayOfWeek: {
      '*': { prefix: '和' }
    },
    day: {
      prefix: '的'
    }
  },
  year: {
    text: '年',
    dayOfWeek: {
      '*': { prefix: '和' }
    }
  }
};

var da = {
  '*': {
    prefix: 'Hver',
    suffix: '',
    text: 'Ukendt',
    '*': {
      empty: { text: 'hver {{field.id}}' },
      value: { text: '{{val.text}}' },
      range: { text: '{{start.text}}-{{end.text}}' },
      everyX: { text: 'hver {{every.value}}' }
    },
    month: {
      '*': { prefix: 'i' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    day: {
      '*': { prefix: 'på' }
    },
    dayOfWeek: {
      '*': { prefix: 'på' },
      empty: { text: 'hver dag i ugen' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    hour: {
      '*': { prefix: 'klokken' }
    },
    minute: {
      '*': { prefix: ':' }
    }
  },
  minute: {
    text: 'Minut'
  },
  hour: {
    text: 'Time',
    minute: {
      '*': {
        prefix: 'på de(t)',
        suffix: 'minutter'
      },
      empty: { text: 'hver' }
    }
  },
  day: {
    text: 'Dag'
  },
  week: {
    text: 'Uge'
  },
  month: {
    text: 'Måned',
    dayOfWeek: {
      '*': { prefix: 'og' }
    }
  },
  year: {
    text: 'År',
    dayOfWeek: {
      '*': { prefix: 'og' }
    }
  }
};

var de = {
  '*': {
    prefix: 'Jede',
    suffix: '',
    text: 'Unknown',
    '*': {
      value: { text: '{{val.text}}' },
      range: { text: '{{start.text}}-{{end.text}}' },
      everyX: { text: 'alle {{every.value}}' }
    },
    month: {
      '*': { prefix: 'im' },
      empty: {
        prefix: 'in',
        text: 'jedem Monat'
      },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    day: {
      '*': { prefix: 'den' },
      empty: {
        prefix: 'an',
        text: 'jedem Tag'
      },
      everyX: {
        prefix: '',
        text: 'alle {{every.value}} Tage'
      }
    },
    dayOfWeek: {
      '*': { prefix: 'am' },
      empty: {
        prefix: 'an',
        text: 'jedem Wochentag'
      },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    hour: {
      '*': { prefix: 'um' },
      empty: {
        prefix: 'zu',
        text: 'jeder Stunde'
      },
      everyX: {
        prefix: '',
        text: 'alle {{every.value}} Stunden'
      }
    },
    minute: {
      '*': { prefix: ':' },
      empty: { text: 'jede Minute' },
      everyX: {
        prefix: '',
        text: 'alle {{every.value}} Minuten'
      }
    }
  },
  minute: {
    text: 'Minute'
  },
  hour: {
    text: 'Stunde',
    minute: {
      '*': {
        prefix: 'zu',
        suffix: 'Minute(n)'
      },
      empty: { text: 'jeder' }
    }
  },
  day: {
    prefix: 'Jeden',
    text: 'Tag'
  },
  week: {
    text: 'Woche'
  },
  month: {
    prefix: 'Jedes',
    text: 'Monat'

  },
  year: {
    prefix: 'Jedes',
    text: 'Jahr'
  }
};

var en = {
  '*': {
    prefix: 'Every',
    suffix: '',
    text: 'Unknown',
    '*': {
      empty: { text: 'every {{field.id}}' },
      value: { text: '{{val.text}}' },
      range: { text: '{{start.text}}-{{end.text}}' },
      everyX: { text: 'every {{every.value}}' }
    },
    month: {
      '*': { prefix: 'in' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    day: {
      '*': { prefix: 'on' }
    },
    dayOfWeek: {
      '*': { prefix: 'on' },
      empty: { text: 'every day of the week' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    hour: {
      '*': { prefix: 'at' }
    },
    minute: {
      '*': { prefix: ':' }
    }
  },
  minute: {
    text: 'Minute'
  },
  hour: {
    text: 'Hour',
    minute: {
      '*': {
        prefix: 'at',
        suffix: 'minute(s)'
      },
      empty: { text: 'every' }
    }
  },
  day: {
    text: 'Day'
  },
  week: {
    text: 'Week'
  },
  month: {
    text: 'Month',
    dayOfWeek: {
      '*': { prefix: 'and' }
    }
  },
  year: {
    text: 'Year',
    dayOfWeek: {
      '*': { prefix: 'and' }
    }
  }
};

var es = {
  '*': {
    prefix: 'todos los',
    suffix: '',
    text: 'Desconocido',
    '*': {
      empty: { text: 'todos los {{ field.id }}' },
      value: { text: '{{ val.text }}' },
      range: { text: '{{ start.text }}-{{ end.text }}' },
      everyX: { text: 'todos/as {{ every.value }}' }
    },
    month: {
      '*': { prefix: 'en' },
      empty: { text: 'todos los meses' },
      value: { text: '{{ val.alt }}' },
      range: { text: '{{ start.alt }}-{{ end.alt }}' }
    },
    day: {
      '*': { prefix: 'en' },
      empty: { text: 'todos los días' },
      value: { text: 'los días {{ val.alt }}' }
    },
    dayOfWeek: {
      '*': { prefix: 'de' },
      empty: { text: 'todos los días de la semana' },
      value: { text: 'los {{ val.alt }}' },
      range: { text: '{{ start.alt }}-{{ end.alt }}' }
    },
    hour: {
      '*': { prefix: 'a' },
      empty: { text: 'todas las horas' },
      value: { text: 'las {{ val.text }}' }
    },
    minute: {
      '*': { prefix: ':' },
      empty: { text: 'todos los minutos' }
    }
  },
  minute: {
    prefix: 'todos los',
    text: 'minutos'
  },
  hour: {
    prefix: 'todas las',
    text: 'horas',
    minute: {
      '*': {
        prefix: 'a los',
        suffix: 'minutos'
      },
      empty: { text: 'todos', prefix: 'a', suffix: 'los minutos' }
    }
  },
  day: {
    text: 'Días'
  },
  week: {
    text: 'Semanas'
  },
  month: {
    text: 'Meses',
    dayOfWeek: {
      '*': { prefix: 'y' }
    }
  },
  year: {
    text: 'años',
    dayOfWeek: {
      '*': { prefix: 'y' }
    }
  }
};

var pt = {
  '*': {
    prefix: 'Todo(a)',
    suffix: '',
    text: 'Desconhecido',
    '*': {
      empty: { text: 'todo {{field.id}}' },
      value: { text: '{{val.text}}' },
      range: { text: '{{start.text}}-{{end.text}}' },
      everyX: { text: 'todo {{every.value}}' }
    },
    month: {
      '*': { prefix: 'de' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' },
      empty: { text: 'todo mês' }
    },
    day: {
      '*': { prefix: 'no(s) dia(s)' },
      empty: { text: 'todos' }
    },
    dayOfWeek: {
      '*': { prefix: 'de' },
      empty: { text: 'todos dias da semana' },
      value: { text: '{{val.alt}}' },
      range: { text: '{{start.alt}}-{{end.alt}}' }
    },
    hour: {
      '*': { prefix: 'às' },
      empty: { text: 'cada hora' }
    },
    minute: {
      '*': { prefix: ':' },
      empty: { text: 'cada minuto' }
    }
  },
  minute: {
    text: 'Minuto'
  },
  hour: {
    text: 'Hora',
    minute: {
      '*': {
        prefix: 'e',
        suffix: 'minuto(s)'
      },
      empty: { text: 'cada' }
    }
  },
  day: {
    text: 'Dia'
  },
  week: {
    text: 'Semana'
  },
  month: {
    text: 'Mês',
    dayOfWeek: {
      '*': { prefix: 'e de' }
    }
  },
  year: {
    text: 'Ano',
    dayOfWeek: {
      '*': { prefix: 'e de' }
    }
  }
};

const { genItems, pad, traverse } = util;

const locales = {
  en,
  de,
  pt,
  es,
  da,
  zh: cn,
  'zh-cn': cn
};

class Locale {
  constructor (dict) {
    this.dict = dict;
  }

  getLocaleStr (...keys) {
    const k = keys.map(key => [key, '*']);
    return traverse(this.dict, ...k) || ''
  }

  render (periodId, fieldId, cronType, position, params) {
    const template = this.getLocaleStr(periodId, fieldId, cronType, position);
    return Mustache.render(template, params || {})
  }
}

/**
 *
 * @param {string} locale=en
 * @param {object} mixin
 * @returns {Locale} Dictionary with all strings in the requested language
 */
function getLocale (locale, mixin) {
  const [language] = locale.split('-');
  const l = locales[locale.toLowerCase()] || locales[language.toLowerCase()] || locales.en;
  const dict = util.deepMerge(l, mixin || {});
  return new Locale(dict)
}

/**
 *
 * @param {string} locale
 * @returns {object} items for minute, hour, day, month and day of week
 */
function defaultItems (locale) {
  return {
    minuteItems: genItems(0, 59, (value) => pad(value, 2)),
    hourItems: genItems(0, 23, (value) => pad(value, 2)),
    dayItems: genItems(1, 31),
    monthItems: genItems(1, 12, (value) => {
      return new Date(2021, value - 1, 1).toLocaleDateString(locale, { month: 'long' })
    }, (value) => {
      return new Date(2021, value - 1, 1).toLocaleDateString(locale, { month: 'short' })
    }),
    dayOfWeekItems: genItems(0, 6, (value) => {
      const date = new Date(2021, 0, 3 + value); // first sunday in 2021
      return date.toLocaleDateString(locale, { weekday: 'long' })
    }, (value) => {
      const date = new Date(2021, 0, 3 + value); // first sunday in 2021
      return date.toLocaleDateString(locale, { weekday: 'short' })
    })
  }
}

var locale = /*#__PURE__*/Object.freeze({
  __proto__: null,
  defaultItems: defaultItems,
  getLocale: getLocale,
  Locale: Locale
});

var script = {
  name: 'VueCronCore',
  props: {
    modelValue: {
      type: String,
      default: '* * * * *'
    },
    locale: {
      type: String,
      default: 'en'
    },
    fields: {
      type: Array,
      default: function (props) {
        const items = defaultItems(props.locale);

        return [
          { id: 'minute', items: items.minuteItems },
          { id: 'hour', items: items.hourItems },
          { id: 'day', items: items.dayItems },
          { id: 'month', items: items.monthItems },
          { id: 'dayOfWeek', items: items.dayOfWeekItems }
        ]
      }
    },
    periods: {
      type: Array,
      default: () => {
        return [
          { id: 'minute', value: [] },
          { id: 'hour', value: ['minute'] },
          { id: 'day', value: ['hour', 'minute'] },
          { id: 'week', value: ['dayOfWeek', 'hour', 'minute'] },
          { id: 'month', value: ['day', 'dayOfWeek', 'hour', 'minute'] },
          { id: 'year', value: ['month', 'day', 'dayOfWeek', 'hour', 'minute'] }
        ]
      }
    },
    customLocale: {
      type: Object,
      default: function (props) {
        return null
      }
    },
    mergeLocale: {
      type: Boolean,
      default: true
    }
  },
  emits: ['update:model-value', 'error'],
  data () {
    const selected = {};
    for (const field of this.fields) {
      selected[field.id] = [];
    }

    return {
      selected,
      error: '',
      selectedPeriod: this.periods[this.periods.length - 1]
    }
  },

  computed: {
    splitValue () {
      return this.modelValue.split(' ')
    },
    fieldIndex () {
      return this.fields.reduce((acc, f, i) => {
        acc[f.id] = i;
        return acc
      }, {})
    },
    periodIndex () {
      return this.periods.reduce((acc, p, i) => {
        acc[p.id] = i;
        return acc
      })
    },
    computedFields () {
      return this.fields.map((f) => new Field(f.id, f.items))
    },
    filteredFields () {
      return this.selectedPeriod.value.map((fieldId) => {
        const i = this.fieldIndex[fieldId];
        return this.computedFields[i]
      })
    },
    _loc () {
      if (this.mergeLocale) {
        return getLocale(this.locale, this.customLocale)
      } else {
        return this.customLocale ? new Locale(this.customLocale) : getLocale(this.locale)
      }
    },
    _periods () {
      if (!this.periods) {
        return []
      }
      return this.periods.map(p => {
        return Object.assign({
          text: this._loc.getLocaleStr(p.id, Position.Text)
        }, p)
      })
    }
  },

  watch: {
    modelValue: {
      handler: function (value) {
        this.cronToSelected(value);
      },
      immediate: true
    },
    selected: {
      handler: function (selected) {
        this.selectedToCron(selected);
      },
      deep: true
    },
    selectedPeriod: {
      handler: function () {
        this.selectedToCron(this.selected);
      }
    },
    error: {
      handler: function (error) {
        this.$emit('error', error);
      }
    }
  },

  render () {
    if (!this.$slots || !this.$slots.default) {
      return
    }

    const fieldProps = [];
    for (const field of this.filteredFields) {
      const i = this.fieldIndex[field.id];
      const values = this.selected[field.id];

      const attrs = {
        modelValue: values
      };
      const events = {
        'update:model-value': ((fieldId) => (evt) => {
          const selected = Array.from(evt).sort((a, b) => { return a > b ? 1 : -1 });
          this.selected[fieldId] = selected;
        })(field.id)
      };

      const cronSegment = multiple.arrayToStr(values, field);
      const segments = Array.isArray(cronSegment.segments) ? cronSegment.segments : [cronSegment];

      const selectedStr = segments.map((seg) => {
        const params = util.populate(seg, field.itemMap);
        params.field = field;
        return this._loc.render(this.selectedPeriod.id, field.id, seg.type, Position.Text, params)
      }).join(',');
      const prefix = this._loc.getLocaleStr(this.selectedPeriod.id, field.id, cronSegment.type, Position.Prefix);
      const suffix = this._loc.getLocaleStr(this.selectedPeriod.id, field.id, cronSegment.type, Position.Suffix);

      fieldProps.push({
        ...field,
        cron: this.splitValue[i],
        selectedStr,
        events,
        attrs,
        prefix,
        suffix
      });
    }

    return this.$slots.default({
      error: this.error,
      fields: fieldProps,

      period: {
        attrs: {
          modelValue: this.selectedPeriod.id
        },
        events: {
          'update:model-value': (periodId) => {
            const i = this.periodIndex[periodId] || 0;
            this.selectedPeriod = this.periods[i];
          }
        },
        items: this._periods,
        prefix: this._loc.getLocaleStr(this.selectedPeriod.id, Position.Prefix),
        suffix: this._loc.getLocaleStr(this.selectedPeriod.id, Position.Suffix)
      }
    })
  },

  methods: {
    defaultValue () {
      return new Array(this.fields.length).fill('*').join(' ')
    },
    cronToSelected (value) {
      if (!value) {
        this.$emit('update:model-value', this.defaultValue());
        return
      }

      if (this.splitValue.length !== this.fields.length) {
        this.error = 'invalid pattern';
        return
      }

      for (let i = 0; i < this.splitValue.length; i++) {
        const field = this.computedFields[i];
        if (!this.selectedPeriod.value.includes(field.id)) {
          continue
        }

        const array = multiple.strToArray(this.splitValue[i], field);
        if (array === null) {
          this.error = 'invalid pattern';
          return
        }
        this.selected[field.id] = array;
      }

      this.error = '';
    },
    selectedToCron (selected) {
      const strings = [];
      for (const field of this.computedFields) {
        if (!this.selectedPeriod.value.includes(field.id)) {
          strings.push('*');
          continue
        }
        const array = selected[field.id];
        const str = multiple.arrayToStr(array, field);
        if (str === null) {
          this.error = 'invalid selection';
          return
        }
        strings.push(str.value);
      }
      this.error = '';
      this.$emit('update:model-value', strings.join(' '));
    }
  }
};

script.__file = "src/core.vue";

// Import vue component

// Declare install function executed by Vue.use()
function install (Vue) {
  if (install.installed) return
  install.installed = true;
  Vue.component('CronCore', script);
}

// Create module definition for Vue.use()
const plugin = {
  install,
  component: script,
  util,
  locale
};

export { script as CronCore, plugin as CronCorePlugin, script$1 as RenderlessSelect, plugin as default, install, locale, util };
