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
        "l5-ex1-1": "работаю",
        "l5-ex1-2": "отдыхаем",
        "l5-ex1-3": "работает",
        "l5-ex1-4": "отдыхают",
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
        const isOk = normalizeText(select.value) === normalizeText(valid);
        select.style.borderColor = isOk ? "#2fbf71" : "#c85757";
        if (isOk)
            correct += 1;
    });

    const result = document.getElementById("l5-result-ex1");
    if (result) {
        result.textContent = hasEmpty
            ? `Правильно: ${correct} из 4. Выберите ответы во всех строках.`
            : `Правильно: ${correct} из 4.`;
    }
    return { correct, total: 4, hasEmpty };
}

function checkExercise2() {
    const answers = {
        "l5-ex2-1": "работает",
        "l5-ex2-2": "отдыхают",
        "l5-ex2-3": "работаете",
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
        const isOk = normalizeText(select.value) === normalizeText(valid);
        select.style.borderColor = isOk ? "#2fbf71" : "#c85757";
        if (isOk)
            correct += 1;
    });

    const result = document.getElementById("l5-result-ex2");
    if (result) {
        result.textContent = hasEmpty
            ? `Правильно: ${correct} из 3. Выберите ответы во всех строках.`
            : `Правильно: ${correct} из 3.`;
    }
    return { correct, total: 3, hasEmpty };
}

function checkExercise3() {
    const answers = {
        "l5-ex3-1": ["что делает антон"],
        "l5-ex3-2": ["что делает твоя сестра"],
        "l5-ex3-3": ["что вы делаете"],
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

    const result = document.getElementById("l5-result-ex3");
    if (result) {
        result.textContent = hasEmpty
            ? `Правильно: ${correct} из 3. Заполните все ответы.`
            : `Правильно: ${correct} из 3.`;
    }
    return { correct, total: 3, hasEmpty };
}

function evaluateVoiceAnswer(transcript) {
    const targetTokens = ["я", "работаю", "а", "мой", "друг", "отдыхает"];
    const normalizedTokens = normalizeText(transcript)
        .split(" ")
        .filter((token) => token.length > 0);
    const uniqueTokens = new Set(normalizedTokens);
    const matchedCount = targetTokens.filter((token) => uniqueTokens.has(token)).length;
    const ratio = matchedCount / targetTokens.length;

    if (ratio === 1) {
        return { passed: true, countedAsPartial: false, completed: true };
    }
    if (ratio >= 0.75 && normalizedTokens.length >= 4) {
        return { passed: true, countedAsPartial: true, completed: true };
    }
    return { passed: false, countedAsPartial: false, completed: true };
}

function initVoiceCheck() {
    const button = document.getElementById("l5-start-voice-check");
    const status = document.getElementById("l5-voice-status");
    const heard = document.getElementById("l5-voice-heard");
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
                status.textContent = 'Почти правильно. Задание засчитано. Эталон: "Я работаю, а мой друг отдыхает."';
            }
            else {
                status.textContent = 'Неправильно. Задание не засчитано. Эталон: "Я работаю, а мой друг отдыхает."';
            }
        };

        recognition.onerror = (event) => {
            voiceCheckState = { passed: false, countedAsPartial: false, completed: false };
            status.textContent = `Ошибка распознавания: ${event.error}. Попробуйте еще раз.`;
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

        finishButton.addEventListener("click", () => {
            readBlock.classList.add("is-hidden");
            writeBlock.classList.remove("is-hidden");
        });

        const checkButton = card.querySelector(".dictation-check");
        if (checkButton) {
            checkButton.addEventListener("click", () => {
                evaluateDictation();
            });
        }
    });
}

function init() {
    document.documentElement.lang = "ru";

    const ex1Button = document.getElementById("l5-check-ex1");
    if (ex1Button) {
        ex1Button.addEventListener("click", () => {
            checkExercise1();
        });
    }

    const ex2Button = document.getElementById("l5-check-ex2");
    if (ex2Button) {
        ex2Button.addEventListener("click", () => {
            checkExercise2();
        });
    }

    const ex3Button = document.getElementById("l5-check-ex3");
    if (ex3Button) {
        ex3Button.addEventListener("click", () => {
            checkExercise3();
        });
    }

    const allButton = document.getElementById("l5-check-all");
    if (allButton) {
        allButton.addEventListener("click", () => {
            const r1 = checkExercise1();
            const r2 = checkExercise2();
            const r3 = checkExercise3();
            const dictation = evaluateDictation();
            const voiceScore = voiceCheckState.passed ? 1 : 0;
            const totalCorrect = r1.correct + r2.correct + r3.correct + dictation.correct + voiceScore;
            const totalTasks = r1.total + r2.total + r3.total + dictation.total + 1;
            const resultAll = document.getElementById("l5-result-all");
            const theoryHint = document.getElementById("l5-theory-hint");
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
                    theoryHint.textContent = 'Голосовое задание не засчитано. Скажите: "Я работаю, а мой друг отдыхает."';
                }
                else if (totalCorrect === totalTasks) {
                    theoryHint.textContent = "Отлично! Ошибок нет.";
                }
                else {
                    theoryHint.innerHTML =
                        'Есть ошибки. Повторите тему и примеры в <a href="docs/textbook/progress_theory.pdf" target="_blank" rel="noopener">учебнике (progress_theory.pdf)</a>.';
                }
            }
        });
    }

    initDictationExercise();
    initVoiceCheck();
}

init();
