"use strict";
function normalizeText(value) {
    return value
        .toLowerCase()
        .replace(/ё/g, "е")
        .replace(/[.,!?;:]/g, "")
        .replace(/\s+/g, " ")
        .trim();
}
let voiceCheckState = {
    passed: false,
    countedAsPartial: false,
    completed: false,
};
function checkExercise1() {
    const answers = {
        "ex1-1": ["это антон он тут", "это антон. он тут"],
        "ex1-2": ["это эмма она там", "это эмма. она там"],
        "ex1-3": ["это мама и папа они дома", "это мама и папа. они дома"],
    };
    let correct = 0;
    let hasEmpty = false;
    Object.entries(answers).forEach(([id, valid]) => {
        const input = document.getElementById(id);
        if (!input)
            return;
        if (!input.value.trim()) {
            input.style.borderColor = "#c85757";
            hasEmpty = true;
            return;
        }
        const value = normalizeText(input.value);
        const isOk = valid.map(normalizeText).includes(value);
        input.style.borderColor = isOk ? "#2fbf71" : "#c85757";
        if (isOk)
            correct += 1;
    });
    const result = document.getElementById("result-ex1");
    if (result) {
        result.textContent = hasEmpty
            ? `Правильно: ${correct} из 3. Заполните все поля.`
            : `Правильно: ${correct} из 3.`;
    }
    return { correct, total: 3, hasEmpty };
}
function checkExercise2() {
    const answers = {
        "ex2-1": "он",
        "ex2-2": "она",
        "ex2-3": "оно",
        "ex2-4": "он",
        "ex2-5": "она",
    };
    let correct = 0;
    let hasEmpty = false;
    Object.entries(answers).forEach(([id, valid]) => {
        const select = document.getElementById(id);
        if (!select)
            return;
        if (!select.value) {
            select.style.borderColor = "#c85757";
            hasEmpty = true;
            return;
        }
        const isOk = select.value === valid;
        select.style.borderColor = isOk ? "#2fbf71" : "#c85757";
        if (isOk)
            correct += 1;
    });
    const result = document.getElementById("result-ex2");
    if (result) {
        result.textContent = hasEmpty
            ? `Правильно: ${correct} из 5. Выберите ответы во всех строках.`
            : `Правильно: ${correct} из 5.`;
    }
    return { correct, total: 5, hasEmpty };
}
function checkExercise3() {
    const answers = {
        "ex3-1": ["да это антон", "да антон"],
        "ex3-2": ["да это парк", "да парк"],
        "ex3-3": ["да это мама", "да мама"],
        "ex3-4": ["да это окно", "да окно"],
    };
    let correct = 0;
    let hasEmpty = false;
    Object.entries(answers).forEach(([id, valid]) => {
        const input = document.getElementById(id);
        if (!input)
            return;
        if (!input.value.trim()) {
            input.style.borderColor = "#c85757";
            hasEmpty = true;
            return;
        }
        const value = normalizeText(input.value);
        const isOk = valid.map(normalizeText).includes(value);
        input.style.borderColor = isOk ? "#2fbf71" : "#c85757";
        if (isOk)
            correct += 1;
    });
    const result = document.getElementById("result-ex3");
    if (result) {
        result.textContent = hasEmpty
            ? `Правильно: ${correct} из 4. Заполните все ответы.`
            : `Правильно: ${correct} из 4.`;
    }
    return { correct, total: 4, hasEmpty };
}
function evaluateVoiceAnswer(transcript) {
    const targetTokens = ["это", "антон", "он", "дома"];
    const normalizedTokens = normalizeText(transcript)
        .split(" ")
        .filter((token) => token.length > 0);
    const uniqueTokens = new Set(normalizedTokens);
    const matchedCount = targetTokens.filter((token) => uniqueTokens.has(token)).length;
    const ratio = matchedCount / targetTokens.length;
    if (ratio === 1) {
        return { passed: true, countedAsPartial: false, completed: true };
    }
    if (ratio >= 0.75 && normalizedTokens.length >= 3) {
        return { passed: true, countedAsPartial: true, completed: true };
    }
    return { passed: false, countedAsPartial: false, completed: true };
}
function initVoiceCheck() {
    const button = document.getElementById("start-voice-check");
    const status = document.getElementById("voice-status");
    const heard = document.getElementById("voice-heard");
    if (!button || !status || !heard)
        return;
    button.addEventListener("click", () => {
        const speechWindow = window;
        const Recognition = speechWindow.SpeechRecognition || speechWindow.webkitSpeechRecognition;
        if (!Recognition) {
            status.textContent = "Распознавание речи не поддерживается в этом браузере.";
            return;
        }
        const recognition = new Recognition();
        recognition.lang = "ru-RU";
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;
        status.textContent = "Слушаю... произнесите фразу.";
        heard.textContent = "";
        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            heard.textContent = `Распознано: ${transcript}`;
            voiceCheckState = evaluateVoiceAnswer(transcript);
            if (voiceCheckState.passed && !voiceCheckState.countedAsPartial) {
                status.textContent = "Хорошо! Фраза произнесена правильно.";
            }
            else if (voiceCheckState.passed && voiceCheckState.countedAsPartial) {
                status.textContent = 'Почти правильно. Задание засчитано. Эталон: "Это Антон. Он дома."';
            }
            else {
                status.textContent = 'Неправильно. Задание не засчитано. Эталон: "Это Антон. Он дома."';
            }
        };
        recognition.onerror = (event) => {
            voiceCheckState = { passed: false, countedAsPartial: false, completed: false };
            status.textContent = `Ошибка распознавания: ${event.error}. Попробуйте ещё раз.`;
        };
        recognition.onend = () => {
            if (!heard.textContent) {
                voiceCheckState = { passed: false, countedAsPartial: false, completed: false };
                status.textContent = "Речь не распознана. Повторите попытку.";
            }
        };
        recognition.start();
    });
}
function evaluateDictation() {
    const cards = document.querySelectorAll(".dictation-card");
    let correct = 0;
    let hasEmpty = false;
    cards.forEach((card) => {
        const input = card.querySelector(".dictation-input");
        const result = card.querySelector(".dictation-result");
        const answerNode = card.querySelector(".dictation-answer");
        const answer = card.dataset.answer ?? "";
        if (!input || !result || !answerNode)
            return;
        if (!input.value.trim()) {
            hasEmpty = true;
            input.style.borderColor = "#c85757";
            result.textContent = "Введите текст по памяти.";
            answerNode.classList.add("is-hidden");
            return;
        }
        const isOk = normalizeText(input.value) === normalizeText(answer);
        input.style.borderColor = isOk ? "#2fbf71" : "#c85757";
        if (isOk) {
            correct += 1;
            result.textContent = "Верно.";
            answerNode.classList.add("is-hidden");
        }
        else {
            result.textContent = "Есть ошибки. Сравните с исходным предложением.";
            answerNode.textContent = `Правильный ответ: ${answer}`;
            answerNode.classList.remove("is-hidden");
        }
    });
    return { correct, total: cards.length, hasEmpty };
}
function initDictationExercise() {
    const cards = document.querySelectorAll(".dictation-card");
    cards.forEach((card) => {
        const finishButton = card.querySelector(".dictation-finish");
        const readBlock = card.querySelector(".dictation-read");
        const writeBlock = card.querySelector(".dictation-write");
        if (!finishButton || !readBlock || !writeBlock)
            return;
        const switchToWriteMode = () => {
            readBlock.classList.add("is-hidden");
            writeBlock.classList.remove("is-hidden");
        };
        finishButton.addEventListener("click", () => {
            switchToWriteMode();
        });
        const checkButton = card.querySelector(".dictation-check");
        if (checkButton) {
            checkButton.addEventListener("click", () => {
                evaluateDictation();
            });
        }
    });
}
function initModulesAccordion() {
    const toggles = document.querySelectorAll(".module-toggle");
    toggles.forEach((toggle) => {
        const content = toggle.nextElementSibling;
        if (!content)
            return;
        const isExpanded = toggle.getAttribute("aria-expanded") === "true";
        if (isExpanded) {
            content.classList.add("is-open");
            content.style.maxHeight = `${content.scrollHeight}px`;
        }
        else {
            content.classList.remove("is-open");
            content.style.maxHeight = "0px";
        }
        toggle.addEventListener("click", () => {
            const expanded = toggle.getAttribute("aria-expanded") === "true";
            if (expanded) {
                toggle.setAttribute("aria-expanded", "false");
                content.style.maxHeight = "0px";
                content.classList.remove("is-open");
            }
            else {
                toggle.setAttribute("aria-expanded", "true");
                content.classList.add("is-open");
                content.style.maxHeight = `${content.scrollHeight}px`;
            }
        });
    });
}
function initLessonButtons() {
    const lessonButtons = document.querySelectorAll(".lesson-open-btn");
    lessonButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const href = button.dataset.href;
            if (!href || button.disabled)
                return;
            window.location.href = href;
        });
    });
}
function init() {
    document.documentElement.lang = "ru";
    const ex1Button = document.getElementById("check-ex1");
    if (ex1Button) {
        ex1Button.addEventListener("click", () => {
            checkExercise1();
        });
    }
    const ex2Button = document.getElementById("check-ex2");
    if (ex2Button) {
        ex2Button.addEventListener("click", () => {
            checkExercise2();
        });
    }
    const ex3Button = document.getElementById("check-ex3");
    if (ex3Button) {
        ex3Button.addEventListener("click", () => {
            checkExercise3();
        });
    }
    const allButton = document.getElementById("check-all");
    if (allButton) {
        allButton.addEventListener("click", () => {
            const r1 = checkExercise1();
            const r2 = checkExercise2();
            const r3 = checkExercise3();
            const dictation = evaluateDictation();
            const voiceScore = voiceCheckState.passed ? 1 : 0;
            const totalCorrect = r1.correct + r2.correct + r3.correct + dictation.correct + voiceScore;
            const totalTasks = r1.total + r2.total + r3.total + dictation.total + 1;
            const resultAll = document.getElementById("result-all");
            const theoryHint = document.getElementById("theory-hint");
            const hasEmpty = r1.hasEmpty || r2.hasEmpty || r3.hasEmpty || dictation.hasEmpty;
            if (resultAll) {
                resultAll.textContent = `Итог: ${totalCorrect} из ${totalTasks}.`;
            }
            if (theoryHint) {
                if (hasEmpty) {
                    theoryHint.textContent = "Сначала заполните все ответы, потом проверьте снова.";
                }
                else if (!voiceCheckState.completed) {
                    theoryHint.textContent = "Сначала выполните голосовое задание.";
                }
                else if (!voiceCheckState.passed) {
                    theoryHint.textContent = 'Голосовое задание не засчитано. Скажите: "Это Антон. Он дома."';
                }
                else if (totalCorrect === totalTasks) {
                    theoryHint.textContent = "Отлично! Ошибок нет.";
                }
                else {
                    theoryHint.innerHTML =
                        'Есть ошибки. Повторите тему и примеры в <a href=\"docs/textbook/progress_theory.pdf\" target=\"_blank\" rel=\"noopener\">учебнике (progress_theory.pdf)</a>.';
                }
            }
        });
    }
    initModulesAccordion();
    initLessonButtons();
    initDictationExercise();
    initVoiceCheck();
}
init();
