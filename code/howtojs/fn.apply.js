Function.prototype.myApply = function(context) {
  const context = context || window;
  context.fn = this;
  let result;
  if (args[1]) {
    result = context.fn(...args[1]);
  } else {
    result = context.fn();
  }
  delete context.fn;
  return result;
}