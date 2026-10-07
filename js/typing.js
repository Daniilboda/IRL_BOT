const texts = {
  ru: [
    "Сегодня у нас урок русского языка в аудитории номер три.",
    "Студенты читают диалог и отвечают на простые вопросы преподавателя.",
    "После пары мы идем в библиотеку и берем новую книгу по грамматике.",
    "На перемене я пью чай и говорю с друзьями о планах на вечер.",
    "В Москве сейчас теплая погода, и в парке много людей.",
    "Я живу в общежитии рядом с университетом и хожу пешком.",
    "По выходным мы гуляем по центру города и фотографируем здания.",
    "На кухне есть стол, стул, холодильник и большая плита.",
    "Моя семья живет в другой стране, но мы часто созваниваемся.",
    "Каждое утро я повторяю новые слова и делаю короткие упражнения.",
    "В магазине можно купить хлеб, молоко, рис, овощи и фрукты.",
    "Мы изучаем падежи постепенно и много тренируемся на примерах.",
    "Сегодня в расписании лекция, практикум и разговорный клуб.",
    "Я пишу сообщение преподавателю и уточняю домашнее задание.",
    "Перед экзаменом важно хорошо отдохнуть и спокойно повторить тему.",
    "фыва олдж фыва олдж фыва олдж фыва олдж фыва олдж",
    "йцукен гшщзх йцукен гшщзх йцукен гшщзх йцукен гшщзх",
    "ячсмить бюэ ячсмить бюэ ячсмить бюэ ячсмить бюэ",
    "съешь еще этих мягких французских булок да выпей чаю"
  ],
  en: [
    "Today we have a Russian class in room three at noon.",
    "Students read a short dialogue and answer simple questions.",
    "After class we go to the library and pick a new book.",
    "On weekends we walk in the city center and take photos.",
    "I live near the university and usually walk to campus.",
    "Every morning I revise new words and write small texts.",
    "At the store you can buy bread, milk, rice, fruit, and tea.",
    "Before the exam it is important to rest and stay calm.",
    "My family lives abroad, but we call each other often.",
    "The weather is warm today, so many people are in the park.",
    "asdf jkl; asdf jkl; asdf jkl; asdf jkl;",
    "qwerty uiop qwerty uiop qwerty uiop",
    "the quick brown fox jumps over the lazy dog",
    "zxcvbnm zxcvbnm zxcvbnm zxcvbnm"
  ]
};

const keyboards = {
  ru: [
    [
      { key: "ё", shift: "Ё", code: "Backquote", finger: "pinky-left" },
      { key: "1", shift: "!", code: "Digit1", finger: "pinky-left" },
      { key: "2", shift: "\"", code: "Digit2", finger: "ring-left" },
      { key: "3", shift: "№", code: "Digit3", finger: "middle-left" },
      { key: "4", shift: ";", code: "Digit4", finger: "index-left" },
      { key: "5", shift: "%", code: "Digit5", finger: "index-left" },
      { key: "6", shift: ":", code: "Digit6", finger: "index-right" },
      { key: "7", shift: "?", code: "Digit7", finger: "index-right" },
      { key: "8", shift: "*", code: "Digit8", finger: "middle-right" },
      { key: "9", shift: "(", code: "Digit9", finger: "ring-right" },
      { key: "0", shift: ")", code: "Digit0", finger: "pinky-right" },
      { key: "-", shift: "_", code: "Minus", finger: "pinky-right" },
      { key: "=", shift: "+", code: "Equal", finger: "pinky-right" },
      { key: "⌫", code: "Backspace", finger: "pinky-right", special: "backspace" }
    ],
    [
      { key: "Tab", code: "Tab", finger: "pinky-left", special: "tab" },
      { key: "й", shift: "Й", code: "KeyQ", finger: "pinky-left" },
      { key: "ц", shift: "Ц", code: "KeyW", finger: "ring-left" },
      { key: "у", shift: "У", code: "KeyE", finger: "middle-left" },
      { key: "к", shift: "К", code: "KeyR", finger: "index-left" },
      { key: "е", shift: "Е", code: "KeyT", finger: "index-left" },
      { key: "н", shift: "Н", code: "KeyY", finger: "index-right" },
      { key: "г", shift: "Г", code: "KeyU", finger: "index-right" },
      { key: "ш", shift: "Ш", code: "KeyI", finger: "middle-right" },
      { key: "щ", shift: "Щ", code: "KeyO", finger: "ring-right" },
      { key: "з", shift: "З", code: "KeyP", finger: "pinky-right" },
      { key: "х", shift: "Х", code: "BracketLeft", finger: "pinky-right" },
      { key: "ъ", shift: "Ъ", code: "BracketRight", finger: "pinky-right" },
      { key: "\\", shift: "/", code: "Backslash", finger: "pinky-right" }
    ],
    [
      { key: "Caps", code: "CapsLock", finger: "pinky-left", special: "caps" },
      { key: "ф", shift: "Ф", code: "KeyA", finger: "pinky-left" },
      { key: "ы", shift: "Ы", code: "KeyS", finger: "ring-left" },
      { key: "в", shift: "В", code: "KeyD", finger: "middle-left" },
      { key: "а", shift: "А", code: "KeyF", finger: "index-left" },
      { key: "п", shift: "П", code: "KeyG", finger: "index-left" },
      { key: "р", shift: "Р", code: "KeyH", finger: "index-right" },
      { key: "о", shift: "О", code: "KeyJ", finger: "index-right" },
      { key: "л", shift: "Л", code: "KeyK", finger: "middle-right" },
      { key: "д", shift: "Д", code: "KeyL", finger: "ring-right" },
      { key: "ж", shift: "Ж", code: "Semicolon", finger: "pinky-right" },
      { key: "э", shift: "Э", code: "Quote", finger: "pinky-right" },
      { key: "Enter", code: "Enter", finger: "pinky-right", special: "enter" }
    ],
    [
      { key: "Shift", code: "ShiftLeft", finger: "pinky-left", special: "shift-left" },
      { key: "я", shift: "Я", code: "KeyZ", finger: "pinky-left" },
      { key: "ч", shift: "Ч", code: "KeyX", finger: "ring-left" },
      { key: "с", shift: "С", code: "KeyC", finger: "middle-left" },
      { key: "м", shift: "М", code: "KeyV", finger: "index-left" },
      { key: "и", shift: "И", code: "KeyB", finger: "index-left" },
      { key: "т", shift: "Т", code: "KeyN", finger: "index-right" },
      { key: "ь", shift: "Ь", code: "KeyM", finger: "index-right" },
      { key: "б", shift: "Б", code: "Comma", finger: "middle-right" },
      { key: "ю", shift: "Ю", code: "Period", finger: "ring-right" },
      { key: ".", shift: ",", code: "Slash", finger: "pinky-right" },
      { key: "Shift", code: "ShiftRight", finger: "pinky-right", special: "shift-right" }
    ],
    [
      { key: "Ctrl", code: "ControlLeft", finger: "pinky-left", special: "ctrl" },
      { key: "Alt", code: "AltLeft", finger: "thumb", special: "alt" },
      { key: " ", code: "Space", finger: "thumb", special: "space" },
      { key: "Alt", code: "AltRight", finger: "thumb", special: "alt" },
      { key: "Ctrl", code: "ControlRight", finger: "pinky-right", special: "ctrl" }
    ]
  ],
  en: [
    [
      { key: "`", shift: "~", code: "Backquote", finger: "pinky-left" },
      { key: "1", shift: "!", code: "Digit1", finger: "pinky-left" },
      { key: "2", shift: "@", code: "Digit2", finger: "ring-left" },
      { key: "3", shift: "#", code: "Digit3", finger: "middle-left" },
      { key: "4", shift: "$", code: "Digit4", finger: "index-left" },
      { key: "5", shift: "%", code: "Digit5", finger: "index-left" },
      { key: "6", shift: "^", code: "Digit6", finger: "index-right" },
      { key: "7", shift: "&", code: "Digit7", finger: "index-right" },
      { key: "8", shift: "*", code: "Digit8", finger: "middle-right" },
      { key: "9", shift: "(", code: "Digit9", finger: "ring-right" },
      { key: "0", shift: ")", code: "Digit0", finger: "pinky-right" },
      { key: "-", shift: "_", code: "Minus", finger: "pinky-right" },
      { key: "=", shift: "+", code: "Equal", finger: "pinky-right" },
      { key: "⌫", code: "Backspace", finger: "pinky-right", special: "backspace" }
    ],
    [
      { key: "Tab", code: "Tab", finger: "pinky-left", special: "tab" },
      { key: "q", shift: "Q", code: "KeyQ", finger: "pinky-left" },
      { key: "w", shift: "W", code: "KeyW", finger: "ring-left" },
      { key: "e", shift: "E", code: "KeyE", finger: "middle-left" },
      { key: "r", shift: "R", code: "KeyR", finger: "index-left" },
      { key: "t", shift: "T", code: "KeyT", finger: "index-left" },
      { key: "y", shift: "Y", code: "KeyY", finger: "index-right" },
      { key: "u", shift: "U", code: "KeyU", finger: "index-right" },
      { key: "i", shift: "I", code: "KeyI", finger: "middle-right" },
      { key: "o", shift: "O", code: "KeyO", finger: "ring-right" },
      { key: "p", shift: "P", code: "KeyP", finger: "pinky-right" },
      { key: "[", shift: "{", code: "BracketLeft", finger: "pinky-right" },
      { key: "]", shift: "}", code: "BracketRight", finger: "pinky-right" },
      { key: "\\", shift: "|", code: "Backslash", finger: "pinky-right" }
    ],
    [
      { key: "Caps", code: "CapsLock", finger: "pinky-left", special: "caps" },
      { key: "a", shift: "A", code: "KeyA", finger: "pinky-left" },
      { key: "s", shift: "S", code: "KeyS", finger: "ring-left" },
      { key: "d", shift: "D", code: "KeyD", finger: "middle-left" },
      { key: "f", shift: "F", code: "KeyF", finger: "index-left" },
      { key: "g", shift: "G", code: "KeyG", finger: "index-left" },
      { key: "h", shift: "H", code: "KeyH", finger: "index-right" },
      { key: "j", shift: "J", code: "KeyJ", finger: "index-right" },
      { key: "k", shift: "K", code: "KeyK", finger: "middle-right" },
      { key: "l", shift: "L", code: "KeyL", finger: "ring-right" },
      { key: ";", shift: ":", code: "Semicolon", finger: "pinky-right" },
      { key: "'", shift: "\"", code: "Quote", finger: "pinky-right" },
      { key: "Enter", code: "Enter", finger: "pinky-right", special: "enter" }
    ],
    [
      { key: "Shift", code: "ShiftLeft", finger: "pinky-left", special: "shift-left" },
      { key: "z", shift: "Z", code: "KeyZ", finger: "pinky-left" },
      { key: "x", shift: "X", code: "KeyX", finger: "ring-left" },
      { key: "c", shift: "C", code: "KeyC", finger: "middle-left" },
      { key: "v", shift: "V", code: "KeyV", finger: "index-left" },
      { key: "b", shift: "B", code: "KeyB", finger: "index-left" },
      { key: "n", shift: "N", code: "KeyN", finger: "index-right" },
      { key: "m", shift: "M", code: "KeyM", finger: "index-right" },
      { key: ",", shift: "<", code: "Comma", finger: "middle-right" },
      { key: ".", shift: ">", code: "Period", finger: "ring-right" },
      { key: "/", shift: "?", code: "Slash", finger: "pinky-right" },
      { key: "Shift", code: "ShiftRight", finger: "pinky-right", special: "shift-right" }
    ],
    [
      { key: "Ctrl", code: "ControlLeft", finger: "pinky-left", special: "ctrl" },
      { key: "Alt", code: "AltLeft", finger: "thumb", special: "alt" },
      { key: " ", code: "Space", finger: "thumb", special: "space" },
      { key: "Alt", code: "AltRight", finger: "thumb", special: "alt" },
      { key: "Ctrl", code: "ControlRight", finger: "pinky-right", special: "ctrl" }
    ]
  ]
};

const state = {
  language: "ru",
  currentText: "",
  currentIndex: 0,
  isRunning: false,
  isPaused: false,
  timerInterval: null,
  totalTime: 180,
  timeLeft: 180,
  correctChars: 0,
  totalChars: 0,
  errors: 0,
  typedText: ""
};

const elements = {
  langRu: document.getElementById("lang-ru"),
  langEn: document.getElementById("lang-en"),
  startBtn: document.getElementById("start-btn"),
  pauseBtn: document.getElementById("pause-btn"),
  restartBtn: document.getElementById("restart-btn"),
  timer: document.getElementById("timer"),
  speed: document.getElementById("speed"),
  accuracy: document.getElementById("accuracy"),
  charsTyped: document.getElementById("chars-typed"),
  textContainer: document.getElementById("text-container"),
  keyboard: document.getElementById("keyboard"),
  resultsModal: document.getElementById("results-modal"),
  resultTime: document.getElementById("result-time"),
  resultSpeed: document.getElementById("result-speed"),
  resultAccuracy: document.getElementById("result-accuracy"),
  resultChars: document.getElementById("result-chars"),
  resultErrors: document.getElementById("result-errors"),
  ratingText: document.getElementById("rating-text"),
  closeModal: document.getElementById("close-modal"),
  pauseOverlay: document.getElementById("pause-overlay")
};

let charToKeyCode = {};

function normalizeChar(char) {
  if (char === "ё") return "е";
  if (char === "Ё") return "Е";
  return char;
}

function buildCharToKeyCode() {
  charToKeyCode = {};
  const layout = keyboards[state.language];

  layout.forEach((row) => {
    row.forEach((keyData) => {
      if (keyData.key && keyData.key.length === 1) {
        charToKeyCode[keyData.key.toLowerCase()] = keyData.code;
        if (keyData.shift) {
          charToKeyCode[keyData.shift.toLowerCase()] = keyData.code;
        }
      }
      if (keyData.special === "space") {
        charToKeyCode[" "] = keyData.code;
      }
    });
  });
}

function renderKeyboard() {
  const layout = keyboards[state.language];
  elements.keyboard.innerHTML = "";

  layout.forEach((row) => {
    const rowDiv = document.createElement("div");
    rowDiv.className = "keyboard-row";

    row.forEach((keyData) => {
      const keyDiv = document.createElement("div");
      keyDiv.className = `key finger-${keyData.finger}`;
      keyDiv.dataset.code = keyData.code;

      if (keyData.special) {
        keyDiv.classList.add(keyData.special);
      }

      keyDiv.textContent = keyData.special === "space" ? "Пробел" : keyData.key;
      rowDiv.appendChild(keyDiv);
    });

    elements.keyboard.appendChild(rowDiv);
  });

  buildCharToKeyCode();
}

function getRandomText() {
  const textList = texts[state.language];
  return textList[Math.floor(Math.random() * textList.length)];
}

function renderText() {
  const chars = state.currentText.split("");
  let html = "";

  chars.forEach((char, index) => {
    let className = "char";

    if (index < state.currentIndex) {
      const typedChar = state.typedText[index];
      if (normalizeChar(typedChar) === normalizeChar(char)) className += " correct";
      else className += " incorrect";
    } else if (index === state.currentIndex) className += " current";
    else className += " pending";

    const displayChar = char === " " ? "&nbsp;" : char;
    html += `<span class="${className}">${displayChar}</span>`;
  });

  elements.textContainer.innerHTML = html;
  highlightKey(state.currentText[state.currentIndex]);
}

function highlightKey(char) {
  document.querySelectorAll(".key").forEach((key) => key.classList.remove("active"));
  if (!char) return;

  const normalizedChar = normalizeChar(char);
  const keyCode = charToKeyCode[normalizedChar.toLowerCase()];
  if (keyCode) {
    const keyElement = document.querySelector(`.key[data-code="${keyCode}"]`);
    if (keyElement) keyElement.classList.add("active");
  }
}

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60);
  const secs = seconds % 60;
  return `${mins}:${secs.toString().padStart(2, "0")}`;
}

function updateTimer() {
  if (state.isPaused) return;
  state.timeLeft -= 1;
  elements.timer.textContent = formatTime(state.timeLeft);
  if (state.timeLeft <= 0) endGame();
}

function updateStats() {
  const elapsedSeconds = state.totalTime - state.timeLeft;
  if (elapsedSeconds > 0) {
    const speed = Math.round((state.correctChars / elapsedSeconds) * 60);
    elements.speed.textContent = `${speed} зн/мин`;
  }
  const accuracy = state.totalChars > 0 ? Math.round((state.correctChars / state.totalChars) * 100) : 100;
  elements.accuracy.textContent = `${accuracy}%`;
  elements.charsTyped.textContent = state.correctChars;
}

function startGame() {
  state.currentText = getRandomText();
  state.currentIndex = 0;
  state.isRunning = true;
  state.isPaused = false;
  state.timeLeft = state.totalTime;
  state.correctChars = 0;
  state.totalChars = 0;
  state.errors = 0;
  state.typedText = "";

  elements.startBtn.classList.add("is-hidden");
  elements.pauseBtn.classList.remove("is-hidden");
  elements.restartBtn.classList.remove("is-hidden");

  elements.langRu.disabled = true;
  elements.langEn.disabled = true;
  elements.timer.textContent = formatTime(state.timeLeft);
  elements.speed.textContent = "0 зн/мин";
  elements.accuracy.textContent = "100%";
  elements.charsTyped.textContent = "0";
  renderText();
  state.timerInterval = setInterval(updateTimer, 1000);
}

function togglePause() {
  if (!state.isRunning) return;
  state.isPaused = !state.isPaused;
  elements.pauseBtn.textContent = state.isPaused ? "Продолжить" : "Пауза";
  elements.pauseOverlay.classList.toggle("visible", state.isPaused);
}

function endGame() {
  state.isRunning = false;
  state.isPaused = false;
  if (state.timerInterval) clearInterval(state.timerInterval);
  state.timerInterval = null;
  elements.pauseBtn.classList.add("is-hidden");
  elements.pauseOverlay.classList.remove("visible");
  showResults();
}

function showResults() {
  const elapsedSeconds = state.totalTime - state.timeLeft;
  const speed = elapsedSeconds > 0 ? Math.round((state.correctChars / elapsedSeconds) * 60) : 0;
  const accuracy = state.totalChars > 0 ? Math.round((state.correctChars / state.totalChars) * 100) : 0;

  elements.resultTime.textContent = formatTime(elapsedSeconds);
  elements.resultSpeed.textContent = String(speed);
  elements.resultAccuracy.textContent = String(accuracy);
  elements.resultChars.textContent = String(state.correctChars);
  elements.resultErrors.textContent = String(state.errors);

  let rating = "";
  if (speed >= 300 && accuracy >= 98) rating = "Мастер печати.";
  else if (speed >= 200 && accuracy >= 95) rating = "Отличный результат.";
  else if (speed >= 150 && accuracy >= 90) rating = "Хороший темп, продолжайте.";
  else if (speed >= 100 && accuracy >= 85) rating = "Неплохо, есть потенциал роста.";
  else if (speed >= 50) rating = "Начальный уровень, больше практики.";
  else rating = "Начало положено, продолжайте тренировки.";

  elements.ratingText.textContent = rating;
  elements.resultsModal.classList.remove("is-hidden");
}

function restartGame() {
  if (state.timerInterval) clearInterval(state.timerInterval);
  state.timerInterval = null;
  state.isRunning = false;
  state.isPaused = false;
  state.typedText = "";

  elements.startBtn.textContent = "Начать печать";
  elements.startBtn.classList.remove("is-hidden");
  elements.pauseBtn.classList.add("is-hidden");
  elements.pauseBtn.textContent = "Пауза";
  elements.restartBtn.classList.add("is-hidden");
  elements.pauseOverlay.classList.remove("visible");
  elements.langRu.disabled = false;
  elements.langEn.disabled = false;
  elements.textContainer.innerHTML = '<p class="placeholder-text">Нажмите "Начать печать" или пробел.</p>';
  elements.timer.textContent = "3:00";
  elements.speed.textContent = "0 зн/мин";
  elements.accuracy.textContent = "100%";
  elements.charsTyped.textContent = "0";
  document.querySelectorAll(".key").forEach((key) => key.classList.remove("active"));
}

function changeLanguage(lang) {
  if (state.isRunning) return;
  state.language = lang;
  elements.langRu.classList.toggle("active", lang === "ru");
  elements.langEn.classList.toggle("active", lang === "en");
  renderKeyboard();
}

function handleTypingKey(key) {
  if (state.isPaused || !state.isRunning) return;
  const currentChar = state.currentText[state.currentIndex];
  state.totalChars += 1;
  const normalizedKey = normalizeChar(key);
  const normalizedCurrentChar = normalizeChar(currentChar);

  if (normalizedKey === normalizedCurrentChar) {
    state.correctChars += 1;
    state.typedText += currentChar;
    state.currentIndex += 1;
    if (state.currentIndex >= state.currentText.length) {
      state.currentText = getRandomText();
      state.currentIndex = 0;
      state.typedText = "";
    }
  } else state.errors += 1;

  renderText();
  updateStats();
}

function handleKeyDown(e) {
  const keyElement = document.querySelector(`.key[data-code="${e.code}"]`);
  if (keyElement) keyElement.classList.add("pressed");

  if (!state.isRunning && e.code === "Space") {
    e.preventDefault();
    startGame();
    return;
  }
  if (state.isRunning && e.code === "Escape") {
    e.preventDefault();
    togglePause();
    return;
  }
  if (state.isPaused) return;

  if (state.isRunning) {
    e.preventDefault();
    let typedChar = null;
    if (e.code === "Space") typedChar = " ";
    else if (e.key.length === 1) typedChar = e.key;
    if (typedChar !== null) handleTypingKey(typedChar);
  }
}

function handleKeyUp(e) {
  const keyElement = document.querySelector(`.key[data-code="${e.code}"]`);
  if (keyElement) keyElement.classList.remove("pressed");
}

function init() {
  renderKeyboard();
  elements.langRu.addEventListener("click", () => changeLanguage("ru"));
  elements.langEn.addEventListener("click", () => changeLanguage("en"));
  elements.startBtn.addEventListener("click", () => {
    if (!state.isRunning) startGame();
  });
  elements.pauseBtn.addEventListener("click", togglePause);
  elements.restartBtn.addEventListener("click", restartGame);
  document.addEventListener("keydown", handleKeyDown);
  document.addEventListener("keyup", handleKeyUp);
  elements.closeModal.addEventListener("click", () => {
    elements.resultsModal.classList.add("is-hidden");
    restartGame();
  });
}

document.addEventListener("DOMContentLoaded", init);
