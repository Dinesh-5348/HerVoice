"use strict";

const languageData = {
  "hi-IN": {
    title: "अपनी भाषा चुनें", start: "शुरू करें", caption: "आपकी बात",
    mic: "बोलने के लिए दबाएँ", stop: "रिकॉर्डिंग रोकें", textLabel: "अपना जवाब लिखें",
    placeholder: "यहाँ लिखें", send: "भेजें", repeat: "कृपया फिर से बोलें।",
    fallback: "अब आप अपना जवाब लिख सकती हैं।", denied: "माइक उपलब्ध नहीं है। आप अपना जवाब लिख सकती हैं।",
    noVoice: "इस भाषा की आवाज़ इस डिवाइस पर उपलब्ध नहीं है। नीचे दिया संदेश पढ़ें।",
    recording: "सुन रही हूँ…", processing: "जवाब देख रही हूँ…", finalKicker: "अगला कदम",
    finalTitle: "यह साथ ले जाएँ", replay: "फिर से शुरू करें",
    questions: ["क्या आप महिला हैं?", "आपकी उम्र कितनी है?", "क्या आपका परिवार गरीब परिवार है?", "क्या आपके घर में पहले से एलपीजी गैस कनेक्शन है?"],
    documents: ["केवाईसी आवेदन पत्र", "आवेदिका का आधार कार्ड", "आधार के पते से अलग हो तो पते का प्रमाण", "राज्य का राशन कार्ड या परिवार का सरकारी दस्तावेज़", "उस दस्तावेज़ में दर्ज वयस्क सदस्यों के आधार कार्ड", "बैंक पासबुक की प्रति या रद्द चेक", "वंचना घोषणा-पत्र"]
  },
  "ta-IN": {
    title: "உங்கள் மொழியைத் தேர்ந்தெடுக்கவும்", start: "தொடங்குங்கள்", caption: "உங்கள் பதில்",
    mic: "பேச அழுத்துங்கள்", stop: "பதிவை நிறுத்துங்கள்", textLabel: "உங்கள் பதிலை எழுதுங்கள்",
    placeholder: "இங்கே எழுதுங்கள்", send: "அனுப்புங்கள்", repeat: "தயவுசெய்து மீண்டும் சொல்லுங்கள்.",
    fallback: "இப்போது உங்கள் பதிலை எழுதலாம்.", denied: "ஒலிவாங்கி கிடைக்கவில்லை. உங்கள் பதிலை எழுதலாம்.",
    noVoice: "இந்த சாதனத்தில் இந்த மொழிக்கான குரல் இல்லை. கீழே உள்ள செய்தியைப் படிக்கவும்.",
    recording: "கேட்கிறது…", processing: "உங்கள் பதிலைப் பார்க்கிறது…", finalKicker: "அடுத்த படி",
    finalTitle: "இவற்றை எடுத்துச் செல்லுங்கள்", replay: "மீண்டும் தொடங்குங்கள்",
    questions: ["நீங்கள் பெண்ணா?", "உங்கள் வயது என்ன?", "உங்கள் குடும்பம் ஏழைக் குடும்பமா?", "உங்கள் வீட்டில் ஏற்கனவே எல்பிஜி இணைப்பு உள்ளதா?"],
    documents: ["KYC விண்ணப்பப் படிவம்", "விண்ணப்பதாரரின் ஆதார் நகல்", "ஆதார் முகவரி வேறாக இருந்தால் முகவரிச் சான்று", "மாநில ரேஷன் அட்டை அல்லது குடும்ப விவர அரசுச் சான்று", "அந்த ஆவணத்தில் உள்ள வயது வந்த குடும்பத்தினரின் ஆதார் நகல்கள்", "வங்கிக் கணக்குப் புத்தக நகல் அல்லது ரத்து செய்யப்பட்ட காசோலை", "வறுமை நிலை அறிவிப்பு"]
  },
  "te-IN": {
    title: "మీ భాషను ఎంచుకోండి", start: "ప్రారంభించండి", caption: "మీ సమాధానం",
    mic: "మాట్లాడటానికి నొక్కండి", stop: "రికార్డింగ్ ఆపండి", textLabel: "మీ సమాధానాన్ని రాయండి",
    placeholder: "ఇక్కడ రాయండి", send: "పంపండి", repeat: "దయచేసి మళ్లీ చెప్పండి.",
    fallback: "ఇప్పుడు మీరు సమాధానాన్ని రాయవచ్చు.", denied: "మైక్రోఫోన్ అందుబాటులో లేదు. మీ సమాధానాన్ని రాయవచ్చు.",
    noVoice: "ఈ పరికరంలో ఈ భాషకు వాయిస్ లేదు. కింద ఉన్న సందేశాన్ని చదవండి.",
    recording: "వింటున్నాను…", processing: "మీ సమాధానాన్ని చూస్తున్నాను…", finalKicker: "తదుపరి అడుగు",
    finalTitle: "వీటిని వెంట తీసుకెళ్లండి", replay: "మళ్లీ ప్రారంభించండి",
    questions: ["మీరు మహిళనా?", "మీ వయస్సు ఎంత?", "మీ కుటుంబం పేద కుటుంబమా?", "మీ ఇంట్లో ఇప్పటికే ఎల్‌పీజీ కనెక్షన్ ఉందా?"],
    documents: ["KYC దరఖాస్తు పత్రం", "దరఖాస్తుదారుని ఆధార్ కాపీ", "ఆధార్‌లోని చిరునామా వేరైతే చిరునామా రుజువు", "రాష్ట్ర రేషన్ కార్డు లేదా కుటుంబ వివరాల ప్రభుత్వ పత్రం", "ఆ పత్రంలో ఉన్న పెద్దల ఆధార్ కాపీలు", "బ్యాంక్ పాస్‌బుక్ కాపీ లేదా రద్దు చేసిన చెక్కు", "పేదరిక స్వీయ ప్రకటన"]
  },
  "bn-IN": {
    title: "আপনার ভাষা বেছে নিন", start: "শুরু করুন", caption: "আপনার উত্তর",
    mic: "বলতে চাপ দিন", stop: "রেকর্ডিং থামান", textLabel: "আপনার উত্তর লিখুন",
    placeholder: "এখানে লিখুন", send: "পাঠান", repeat: "দয়া করে আবার বলুন।",
    fallback: "এখন আপনি উত্তরটি লিখতে পারেন।", denied: "মাইক্রোফোন পাওয়া যাচ্ছে না। আপনি উত্তরটি লিখতে পারেন।",
    noVoice: "এই যন্ত্রে এই ভাষার কণ্ঠস্বর নেই। নিচের বার্তাটি পড়ুন।",
    recording: "শুনছি…", processing: "আপনার উত্তর দেখছি…", finalKicker: "পরের ধাপ",
    finalTitle: "এগুলি সঙ্গে নিন", replay: "আবার শুরু করুন",
    questions: ["আপনি কি নারী?", "আপনার বয়স কত?", "আপনার পরিবার কি দরিদ্র পরিবার?", "আপনার বাড়িতে কি আগে থেকেই এলপিজি সংযোগ আছে?"],
    documents: ["কেওয়াইসি আবেদনপত্র", "আবেদনকারীর আধার কার্ডের কপি", "আধারের ঠিকানা আলাদা হলে ঠিকানার প্রমাণ", "রাজ্য রেশন কার্ড বা পরিবারের সরকারি নথি", "ওই নথিতে থাকা প্রাপ্তবয়স্কদের আধার কপি", "ব্যাঙ্কের পাসবইয়ের কপি বা বাতিল চেক", "দারিদ্র্য সংক্রান্ত ঘোষণা"]
  },
  "mr-IN": {
    title: "तुमची भाषा निवडा", start: "सुरू करा", caption: "तुमचे उत्तर",
    mic: "बोलण्यासाठी दाबा", stop: "रेकॉर्डिंग थांबवा", textLabel: "तुमचे उत्तर लिहा",
    placeholder: "इथे लिहा", send: "पाठवा", repeat: "कृपया पुन्हा सांगा.",
    fallback: "आता तुम्ही तुमचे उत्तर लिहू शकता.", denied: "मायक्रोफोन उपलब्ध नाही. तुम्ही तुमचे उत्तर लिहू शकता.",
    noVoice: "या उपकरणावर या भाषेचा आवाज उपलब्ध नाही. खालील संदेश वाचा.",
    recording: "ऐकत आहे…", processing: "तुमचे उत्तर पाहत आहे…", finalKicker: "पुढची पायरी",
    finalTitle: "या गोष्टी सोबत घ्या", replay: "पुन्हा सुरू करा",
    questions: ["तुम्ही महिला आहात का?", "तुमचे वय किती आहे?", "तुमचे कुटुंब गरीब आहे का?", "तुमच्या घरी आधीपासून एलपीजी जोडणी आहे का?"],
    documents: ["केवायसी अर्ज", "अर्जदाराच्या आधार कार्डची प्रत", "आधारवरील पत्ता वेगळा असल्यास पत्त्याचा पुरावा", "राज्याचे रेशन कार्ड किंवा कुटुंबाचा सरकारी दाखला", "त्या दाखल्यातील प्रौढ सदस्यांच्या आधार प्रती", "बँक पासबुकची प्रत किंवा रद्द केलेला धनादेश", "वंचिततेचे घोषणापत्र"]
  },
  "kn-IN": {
    title: "ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ", start: "ಪ್ರಾರಂಭಿಸಿ", caption: "ನಿಮ್ಮ ಉತ್ತರ",
    mic: "ಮಾತನಾಡಲು ಒತ್ತಿರಿ", stop: "ರೆಕಾರ್ಡಿಂಗ್ ನಿಲ್ಲಿಸಿ", textLabel: "ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಬರೆಯಿರಿ",
    placeholder: "ಇಲ್ಲಿ ಬರೆಯಿರಿ", send: "ಕಳುಹಿಸಿ", repeat: "ದಯವಿಟ್ಟು ಮತ್ತೆ ಹೇಳಿ.",
    fallback: "ಈಗ ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಬರೆಯಬಹುದು.", denied: "ಮೈಕ್ರೊಫೋನ್ ಲಭ್ಯವಿಲ್ಲ. ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಬರೆಯಬಹುದು.",
    noVoice: "ಈ ಸಾಧನದಲ್ಲಿ ಈ ಭಾಷೆಯ ಧ್ವನಿ ಲಭ್ಯವಿಲ್ಲ. ಕೆಳಗಿನ ಸಂದೇಶವನ್ನು ಓದಿ.",
    recording: "ಕೇಳುತ್ತಿದ್ದೇನೆ…", processing: "ನಿಮ್ಮ ಉತ್ತರವನ್ನು ನೋಡುತ್ತಿದ್ದೇನೆ…", finalKicker: "ಮುಂದಿನ ಹಂತ",
    finalTitle: "ಇವುಗಳನ್ನು ಜೊತೆಗೆ ತೆಗೆದುಕೊಂಡು ಹೋಗಿ", replay: "ಮತ್ತೆ ಪ್ರಾರಂಭಿಸಿ",
    questions: ["ನೀವು ಮಹಿಳೆಯೇ?", "ನಿಮ್ಮ ವಯಸ್ಸು ಎಷ್ಟು?", "ನಿಮ್ಮ ಕುಟುಂಬ ಬಡ ಕುಟುಂಬವೇ?", "ನಿಮ್ಮ ಮನೆಯಲ್ಲಿ ಈಗಾಗಲೇ ಎಲ್‌ಪಿಜಿ ಸಂಪರ್ಕವಿದೆಯೇ?"],
    documents: ["ಕೆವೈಸಿ ಅರ್ಜಿ ನಮೂನೆ", "ಅರ್ಜಿದಾರರ ಆಧಾರ್ ಪ್ರತಿ", "ಆಧಾರ್‌ನ ವಿಳಾಸ ಬೇರೆ ಇದ್ದರೆ ವಿಳಾಸದ ಪುರಾವೆ", "ರಾಜ್ಯದ ಪಡಿತರ ಚೀಟಿ ಅಥವಾ ಕುಟುಂಬದ ಸರ್ಕಾರಿ ದಾಖಲೆ", "ಆ ದಾಖಲೆಯಲ್ಲಿರುವ ವಯಸ್ಕರ ಆಧಾರ್ ಪ್ರತಿಗಳು", "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಪ್ರತಿ ಅಥವಾ ರದ್ದುಪಡಿಸಿದ ಚೆಕ್", "ವಂಚಿತ ಸ್ಥಿತಿಯ ಘೋಷಣೆ"]
  }
};

const questionIds = ["applicant_is_woman", "applicant_age", "poor_household", "household_has_lpg"];
const languageButtons = [...document.querySelectorAll("[data-language]")];
const welcomeScreen = document.getElementById("welcome-screen");
const guideScreen = document.getElementById("guide-screen");
const finalScreen = document.getElementById("final-screen");
const startButton = document.getElementById("start-button");
const micButton = document.getElementById("mic-button");
const textForm = document.getElementById("text-form");
const textInput = document.getElementById("text-input");
const replyCaption = document.getElementById("reply-caption");
const voiceStatus = document.getElementById("voice-status");
const documentChecklist = document.getElementById("document-checklist");

let language = "hi-IN";
let state = { answers: {}, step: 0 };
let currentQuestionId = questionIds[0];
let currentQuestionText = "";
let silenceCount = 0;
let fallbackEnabled = false;
let recorder = null;
let mediaStream = null;
let audioContext = null;
let analyser = null;
let animationFrame = 0;
let chunks = [];
let recordingStartedAt = 0;
let lastVoiceAt = 0;
let stoppedForSilence = false;
let stopTimer = 0;
let waitingForTurn = false;

const icons = {
  "file-text": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M8 4h11l6 6v18H8zM19 4v7h6M12 16h9M12 21h9"/></svg>',
  "id-card": '<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="4" y="6" width="24" height="20" rx="3"/><circle cx="12" cy="14" r="3"/><path d="M7 22c1-3 9-3 10 0M20 13h4M20 18h4"/></svg>',
  "map-pin": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M25 13c0 7-9 15-9 15S7 20 7 13a9 9 0 1 1 18 0Z"/><circle cx="16" cy="13" r="3"/></svg>',
  users: '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="12" cy="11" r="4"/><circle cx="22" cy="13" r="3"/><path d="M4 26c0-6 3-9 8-9s8 3 8 9M21 19c4 0 7 2 7 7"/></svg>',
  landmark: '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="m4 12 12-8 12 8M6 14h20M8 14v12M14 14v12M20 14v12M26 14v12M4 27h24"/></svg>',
  "file-check": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M8 4h11l6 6v18H8zM19 4v7h6M12 20l3 3 6-7"/></svg>'
};

function words() {
  return languageData[language];
}

function updateLanguage(nextLanguage) {
  language = nextLanguage;
  const text = words();
  document.documentElement.lang = language;
  document.getElementById("welcome-title").textContent = text.title;
  document.getElementById("start-label").textContent = text.start;
  document.getElementById("caption-heading").textContent = text.caption;
  document.getElementById("mic-label").textContent = recorder?.state === "recording" ? text.stop : text.mic;
  document.getElementById("text-label").textContent = text.textLabel;
  textInput.placeholder = text.placeholder;
  document.getElementById("send-button").textContent = text.send;
  document.getElementById("final-kicker").textContent = text.finalKicker;
  document.getElementById("final-heading").textContent = text.finalTitle;
  document.getElementById("replay-button").textContent = text.replay;
  document.getElementById("language-list").setAttribute("aria-label", text.title);
  documentChecklist.setAttribute("aria-label", text.finalTitle);
  for (const id of ["welcome-title", "start-label", "caption-heading", "reply-caption", "voice-status", "mic-label", "text-label", "text-input", "send-button", "final-kicker", "final-heading", "final-caption", "document-checklist", "replay-button"]) {
    document.getElementById(id).setAttribute("lang", language);
  }
  micButton.setAttribute("aria-label", text.mic);
  startButton.setAttribute("aria-label", text.start);
  for (const button of languageButtons) {
    const selected = button.dataset.language === language;
    button.setAttribute("aria-pressed", String(selected));
    button.classList.toggle("is-selected", selected);
  }
}

function setCaption(text) {
  currentQuestionText = text;
  replyCaption.textContent = text;
  replyCaption.lang = language;
}

function findVoice(locale) {
  const voices = window.speechSynthesis?.getVoices() || [];
  const normalized = locale.toLowerCase();
  return voices.find((voice) => voice.lang.toLowerCase() === normalized)
    || voices.find((voice) => voice.lang.toLowerCase().startsWith(`${normalized.split("-")[0]}-`));
}

function speak(text) {
  if (!window.speechSynthesis || !window.SpeechSynthesisUtterance) {
    voiceStatus.textContent = words().noVoice;
    return;
  }
  const voice = findVoice(language);
  if (!voice) {
    voiceStatus.textContent = words().noVoice;
    return;
  }
  voiceStatus.textContent = "";
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = language;
  utterance.voice = voice;
  utterance.rate = 0.88;
  window.speechSynthesis.speak(utterance);
}

function showTextFallback(message) {
  fallbackEnabled = true;
  textForm.hidden = false;
  voiceStatus.textContent = message;
  textInput.focus();
}

function renderChecklist(items) {
  documentChecklist.replaceChildren();
  items.forEach((item, index) => {
    const row = document.createElement("li");
    row.className = "document-item";
    const icon = document.createElement("span");
    icon.className = "document-icon";
    icon.setAttribute("aria-hidden", "true");
    icon.innerHTML = icons[item.icon_name] || icons["file-text"];
    const label = document.createElement("span");
    label.textContent = words().documents[index] || item.label;
    label.lang = language;
    row.append(icon, label);
    documentChecklist.append(row);
  });
}

async function sendTurn({ text = null, blob = null } = {}) {
  if (waitingForTurn) return;
  waitingForTurn = true;
  voiceStatus.textContent = words().processing;
  let payload = { text, lang_hint: language, state };
  if (blob) {
    const bytes = new Uint8Array(await blob.arrayBuffer());
    let binary = "";
    for (let offset = 0; offset < bytes.length; offset += 0x8000) {
      binary += String.fromCharCode(...bytes.subarray(offset, offset + 0x8000));
    }
    payload = { audio_b64: btoa(binary), mime: blob.type || "audio/webm", lang_hint: language, state };
  }
  try {
    const response = await fetch("/api/turn", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (!response.ok) throw new Error("turn failed");
    const result = await response.json();
    language = result.lang;
    state = result.state;
    updateLanguage(language);
    silenceCount = 0;
    if (state.step < questionIds.length) currentQuestionId = questionIds[state.step];
    setCaption(result.reply_text);
    voiceStatus.textContent = "";
    if (result.done) {
      document.getElementById("final-caption").textContent = result.reply_text;
      document.getElementById("final-caption").lang = language;
      renderChecklist(result.checklist);
      guideScreen.hidden = true;
      finalScreen.hidden = false;
    }
    speak(result.reply_text);
    if (!fallbackEnabled && !result.done) textForm.hidden = true;
  } catch {
    showTextFallback(words().fallback);
  } finally {
    waitingForTurn = false;
  }
}

function cleanupAudio() {
  cancelAnimationFrame(animationFrame);
  clearTimeout(stopTimer);
  if (mediaStream) mediaStream.getTracks().forEach((track) => track.stop());
  if (audioContext && audioContext.state !== "closed") audioContext.close();
  mediaStream = null;
  audioContext = null;
  analyser = null;
}

function finishRecording() {
  if (recorder?.state === "recording") recorder.stop();
}

function watchForSilence() {
  if (!analyser || recorder?.state !== "recording") return;
  const samples = new Uint8Array(analyser.fftSize);
  analyser.getByteTimeDomainData(samples);
  let energy = 0;
  for (const sample of samples) {
    const centered = (sample - 128) / 128;
    energy += centered * centered;
  }
  const now = Date.now();
  if (Math.sqrt(energy / samples.length) > 0.018) lastVoiceAt = now;
  if (now - recordingStartedAt > 1200 && now - lastVoiceAt > 3800) {
    stoppedForSilence = true;
    finishRecording();
    return;
  }
  if (now - recordingStartedAt > 20000) {
    finishRecording();
    return;
  }
  animationFrame = requestAnimationFrame(watchForSilence);
}

async function beginRecording() {
  if (waitingForTurn) return;
  if (!navigator.mediaDevices?.getUserMedia || !window.MediaRecorder) {
    showTextFallback(words().denied);
    return;
  }
  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mimeType = ["audio/webm;codecs=opus", "audio/webm", "audio/mp4"]
      .find((type) => MediaRecorder.isTypeSupported(type));
    recorder = mimeType ? new MediaRecorder(mediaStream, { mimeType }) : new MediaRecorder(mediaStream);
    chunks = [];
    stoppedForSilence = false;
    recordingStartedAt = Date.now();
    lastVoiceAt = recordingStartedAt;
    recorder.ondataavailable = (event) => {
      if (event.data.size) chunks.push(event.data);
    };
    recorder.onstop = async () => {
      const wasSilent = stoppedForSilence;
      const recording = new Blob(chunks, { type: recorder.mimeType || "audio/webm" });
      micButton.classList.remove("is-recording");
      micButton.setAttribute("aria-pressed", "false");
      document.getElementById("mic-label").textContent = words().mic;
      cleanupAudio();
      recorder = null;
      if (wasSilent || recording.size === 0) {
        silenceCount += 1;
        if (silenceCount === 1) {
          replyCaption.textContent = currentQuestionText;
          voiceStatus.textContent = words().repeat;
          speak(currentQuestionText);
        } else {
          showTextFallback(words().fallback);
        }
        return;
      }
      await sendTurn({ blob: recording });
    };
    recorder.start(250);
    micButton.classList.add("is-recording");
    micButton.setAttribute("aria-pressed", "true");
    document.getElementById("mic-label").textContent = words().stop;
    voiceStatus.textContent = words().recording;
    try {
      audioContext = new AudioContext();
      analyser = audioContext.createAnalyser();
      analyser.fftSize = 512;
      audioContext.createMediaStreamSource(mediaStream).connect(analyser);
      animationFrame = requestAnimationFrame(watchForSilence);
    } catch {
      stopTimer = window.setTimeout(finishRecording, 20000);
    }
  } catch {
    cleanupAudio();
    showTextFallback(words().denied);
  }
}

function startFlow() {
  state = { answers: {}, step: 0 };
  currentQuestionId = questionIds[0];
  silenceCount = 0;
  fallbackEnabled = false;
  voiceStatus.textContent = "";
  textForm.hidden = true;
  welcomeScreen.hidden = true;
  finalScreen.hidden = true;
  guideScreen.hidden = false;
  const firstQuestion = words().questions[0];
  setCaption(firstQuestion);
  speak(firstQuestion);
}

languageButtons.forEach((button) => {
  button.addEventListener("click", () => updateLanguage(button.dataset.language));
});
startButton.addEventListener("click", startFlow);
micButton.addEventListener("click", () => {
  if (recorder?.state === "recording") finishRecording();
  else beginRecording();
});
textForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const text = textInput.value.trim();
  if (!text) return;
  textInput.value = "";
  await sendTurn({ text });
});
document.getElementById("replay-button").addEventListener("click", startFlow);

updateLanguage(language);