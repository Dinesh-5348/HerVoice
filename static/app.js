"use strict";

const languageData = {
  "hi-IN": {
    title: "अपनी भाषा चुनें", start: "शुरू करें", caption: "आपकी बात", greeting: "नमस्ते।",
    mic: "बोलने के लिए दबाएँ", stop: "रिकॉर्डिंग रोकें", textLabel: "अपना जवाब लिखें",
    placeholder: "यहाँ लिखें", send: "भेजें", repeat: "कृपया फिर से बोलें।",
    fallback: "अब आप अपना जवाब लिख सकती हैं।", denied: "माइक उपलब्ध नहीं है। आप अपना जवाब लिख सकती हैं।",
    noVoice: "इस भाषा की आवाज़ इस डिवाइस पर उपलब्ध नहीं है। नीचे दिया संदेश पढ़ें।",
    unavailable: "सेवा अभी उपलब्ध नहीं है। कृपया बाद में कोशिश करें।",
    recording: "सुन रही हूँ…", processing: "जवाब देख रही हूँ…", finalKicker: "अगला कदम",
    finalTitle: "यह साथ ले जाएँ", replay: "फिर से शुरू करें",
    firstQuestion: "क्या आप महिला हैं?", languageGroup: "भाषा चुनें", conversationLabel: "बातचीत",
    documentList: "दस्तावेज़ों की सूची", yes: "हाँ", no: "नहीं", yesAnswer: "हाँ", noAnswer: "नहीं",
    spokenAnswer: "मैंने बोलकर जवाब दिया।", progress: "प्रश्न", repeatMessage: "यह संदेश फिर सुनें",
    thinking: "सोच रही हूँ…", speaking: "बोल रही हूँ…",
    documents: ["केवाईसी आवेदन पत्र", "आवेदिका का आधार कार्ड", "आधार के पते से अलग हो तो पते का प्रमाण", "राज्य का राशन कार्ड या परिवार का सरकारी दस्तावेज़", "उस दस्तावेज़ में दर्ज वयस्क सदस्यों के आधार कार्ड", "बैंक पासबुक की प्रति या रद्द चेक", "वंचना घोषणा-पत्र"]
  },
  "ta-IN": {
    title: "உங்கள் மொழியைத் தேர்ந்தெடுக்கவும்", start: "தொடங்குங்கள்", caption: "உங்கள் பதில்", greeting: "வணக்கம்.",
    mic: "பேச அழுத்துங்கள்", stop: "பதிவை நிறுத்துங்கள்", textLabel: "உங்கள் பதிலை எழுதுங்கள்",
    placeholder: "இங்கே எழுதுங்கள்", send: "அனுப்புங்கள்", repeat: "தயவுசெய்து மீண்டும் சொல்லுங்கள்.",
    fallback: "இப்போது உங்கள் பதிலை எழுதலாம்.", denied: "ஒலிவாங்கி கிடைக்கவில்லை. உங்கள் பதிலை எழுதலாம்.",
    noVoice: "இந்த சாதனத்தில் இந்த மொழிக்கான குரல் இல்லை. கீழே உள்ள செய்தியைப் படிக்கவும்.",
    unavailable: "சேவை இப்போது கிடைக்கவில்லை. பின்னர் முயற்சிக்கவும்.",
    recording: "கேட்கிறது…", processing: "உங்கள் பதிலைப் பார்க்கிறது…", finalKicker: "அடுத்த படி",
    finalTitle: "இவற்றை எடுத்துச் செல்லுங்கள்", replay: "மீண்டும் தொடங்குங்கள்",
    firstQuestion: "நீங்கள் பெண்ணா?", languageGroup: "மொழியைத் தேர்ந்தெடுக்கவும்", conversationLabel: "உரையாடல்",
    documentList: "ஆவணப் பட்டியல்", yes: "ஆம்", no: "இல்லை", yesAnswer: "ஆம்", noAnswer: "இல்லை",
    spokenAnswer: "பேசிப் பதிலளித்தேன்.", progress: "கேள்வி", repeatMessage: "இந்தச் செய்தியை மீண்டும் கேளுங்கள்",
    thinking: "யோசிக்கிறது…", speaking: "பேசுகிறது…",
    documents: ["KYC விண்ணப்பப் படிவம்", "விண்ணப்பதாரரின் ஆதார் நகல்", "ஆதார் முகவரி வேறாக இருந்தால் முகவரிச் சான்று", "மாநில ரேஷன் அட்டை அல்லது குடும்ப விவர அரசுச் சான்று", "அந்த ஆவணத்தில் உள்ள வயது வந்த குடும்பத்தினரின் ஆதார் நகல்கள்", "வங்கிக் கணக்குப் புத்தக நகல் அல்லது ரத்து செய்யப்பட்ட காசோலை", "வறுமை நிலை அறிவிப்பு"]
  },
  "te-IN": {
    title: "మీ భాషను ఎంచుకోండి", start: "ప్రారంభించండి", caption: "మీ సమాధానం", greeting: "నమస్కారం.",
    mic: "మాట్లాడటానికి నొక్కండి", stop: "రికార్డింగ్ ఆపండి", textLabel: "మీ సమాధానాన్ని రాయండి",
    placeholder: "ఇక్కడ రాయండి", send: "పంపండి", repeat: "దయచేసి మళ్లీ చెప్పండి.",
    fallback: "ఇప్పుడు మీరు సమాధానాన్ని రాయవచ్చు.", denied: "మైక్రోఫోన్ అందుబాటులో లేదు. మీ సమాధానాన్ని రాయవచ్చు.",
    noVoice: "ఈ పరికరంలో ఈ భాషకు వాయిస్ లేదు. కింద ఉన్న సందేశాన్ని చదవండి.",
    unavailable: "సేవ ఇప్పుడు అందుబాటులో లేదు. తర్వాత ప్రయత్నించండి.",
    recording: "వింటున్నాను…", processing: "మీ సమాధానాన్ని చూస్తున్నాను…", finalKicker: "తదుపరి అడుగు",
    finalTitle: "వీటిని వెంట తీసుకెళ్లండి", replay: "మళ్లీ ప్రారంభించండి",
    firstQuestion: "మీరు మహిళనా?", languageGroup: "భాషను ఎంచుకోండి", conversationLabel: "సంభాషణ",
    documentList: "పత్రాల జాబితా", yes: "అవును", no: "కాదు", yesAnswer: "అవును", noAnswer: "కాదు",
    spokenAnswer: "నేను మాట్లాడి సమాధానం ఇచ్చాను.", progress: "ప్రశ్న", repeatMessage: "ఈ సందేశాన్ని మళ్లీ వినండి",
    thinking: "ఆలోచిస్తున్నాను…", speaking: "మాట్లాడుతున్నాను…",
    documents: ["KYC దరఖాస్తు పత్రం", "దరఖాస్తుదారుని ఆధార్ కాపీ", "ఆధార్‌లోని చిరునామా వేరైతే చిరునామా రుజువు", "రాష్ట్ర రేషన్ కార్డు లేదా కుటుంబ వివరాల ప్రభుత్వ పత్రం", "ఆ పత్రంలో ఉన్న పెద్దల ఆధార్ కాపీలు", "బ్యాంక్ పాస్‌బుక్ కాపీ లేదా రద్దు చేసిన చెక్కు", "పేదరిక స్వీయ ప్రకటన"]
  },
  "bn-IN": {
    title: "আপনার ভাষা বেছে নিন", start: "শুরু করুন", caption: "আপনার উত্তর", greeting: "নমস্কার।",
    mic: "বলতে চাপ দিন", stop: "রেকর্ডিং থামান", textLabel: "আপনার উত্তর লিখুন",
    placeholder: "এখানে লিখুন", send: "পাঠান", repeat: "দয়া করে আবার বলুন।",
    fallback: "এখন আপনি উত্তরটি লিখতে পারেন।", denied: "মাইক্রোফোন পাওয়া যাচ্ছে না। আপনি উত্তরটি লিখতে পারেন।",
    noVoice: "এই যন্ত্রে এই ভাষার কণ্ঠস্বর নেই। নিচের বার্তাটি পড়ুন।",
    unavailable: "পরিষেবা এখন পাওয়া যাচ্ছে না। পরে চেষ্টা করুন।",
    recording: "শুনছি…", processing: "আপনার উত্তর দেখছি…", finalKicker: "পরের ধাপ",
    finalTitle: "এগুলি সঙ্গে নিন", replay: "আবার শুরু করুন",
    firstQuestion: "আপনি কি নারী?", languageGroup: "ভাষা বেছে নিন", conversationLabel: "কথোপকথন",
    documentList: "নথির তালিকা", yes: "হ্যাঁ", no: "না", yesAnswer: "হ্যাঁ", noAnswer: "না",
    spokenAnswer: "আমি কথা বলে উত্তর দিয়েছি।", progress: "প্রশ্ন", repeatMessage: "এই বার্তাটি আবার শুনুন",
    thinking: "ভাবছি…", speaking: "বলছি…",
    documents: ["কেওয়াইসি আবেদনপত্র", "আবেদনকারীর আধার কার্ডের কপি", "আধারের ঠিকানা আলাদা হলে ঠিকানার প্রমাণ", "রাজ্য রেশন কার্ড বা পরিবারের সরকারি নথি", "ওই নথিতে থাকা প্রাপ্তবয়স্কদের আধার কপি", "ব্যাঙ্কের পাসবইয়ের কপি বা বাতিল চেক", "দারিদ্র্য সংক্রান্ত ঘোষণা"]
  },
  "mr-IN": {
    title: "तुमची भाषा निवडा", start: "सुरू करा", caption: "तुमचे उत्तर", greeting: "नमस्कार.",
    mic: "बोलण्यासाठी दाबा", stop: "रेकॉर्डिंग थांबवा", textLabel: "तुमचे उत्तर लिहा",
    placeholder: "इथे लिहा", send: "पाठवा", repeat: "कृपया पुन्हा सांगा.",
    fallback: "आता तुम्ही तुमचे उत्तर लिहू शकता.", denied: "मायक्रोफोन उपलब्ध नाही. तुम्ही तुमचे उत्तर लिहू शकता.",
    noVoice: "या उपकरणावर या भाषेचा आवाज उपलब्ध नाही. खालील संदेश वाचा.",
    unavailable: "सेवा आत्ता उपलब्ध नाही. नंतर प्रयत्न करा.",
    recording: "ऐकत आहे…", processing: "तुमचे उत्तर पाहत आहे…", finalKicker: "पुढची पायरी",
    finalTitle: "या गोष्टी सोबत घ्या", replay: "पुन्हा सुरू करा",
    firstQuestion: "तुम्ही महिला आहात का?", languageGroup: "भाषा निवडा", conversationLabel: "संभाषण",
    documentList: "कागदपत्रांची यादी", yes: "हो", no: "नाही", yesAnswer: "हो", noAnswer: "नाही",
    spokenAnswer: "मी बोलून उत्तर दिले.", progress: "प्रश्न", repeatMessage: "हा संदेश पुन्हा ऐका",
    thinking: "विचार करत आहे…", speaking: "बोलत आहे…",
    documents: ["केवायसी अर्ज", "अर्जदाराच्या आधार कार्डची प्रत", "आधारवरील पत्ता वेगळा असल्यास पत्त्याचा पुरावा", "राज्याचे रेशन कार्ड किंवा कुटुंबाचा सरकारी दाखला", "त्या दाखल्यातील प्रौढ सदस्यांच्या आधार प्रती", "बँक पासबुकची प्रत किंवा रद्द केलेला धनादेश", "वंचिततेचे घोषणापत्र"]
  },
  "kn-IN": {
    title: "ನಿಮ್ಮ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ", start: "ಪ್ರಾರಂಭಿಸಿ", caption: "ನಿಮ್ಮ ಉತ್ತರ", greeting: "ನಮಸ್ಕಾರ.",
    mic: "ಮಾತನಾಡಲು ಒತ್ತಿರಿ", stop: "ರೆಕಾರ್ಡಿಂಗ್ ನಿಲ್ಲಿಸಿ", textLabel: "ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಬರೆಯಿರಿ",
    placeholder: "ಇಲ್ಲಿ ಬರೆಯಿರಿ", send: "ಕಳುಹಿಸಿ", repeat: "ದಯವಿಟ್ಟು ಮತ್ತೆ ಹೇಳಿ.",
    fallback: "ಈಗ ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಬರೆಯಬಹುದು.", denied: "ಮೈಕ್ರೊಫೋನ್ ಲಭ್ಯವಿಲ್ಲ. ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಬರೆಯಬಹುದು.",
    noVoice: "ಈ ಸಾಧನದಲ್ಲಿ ಈ ಭಾಷೆಯ ಧ್ವನಿ ಲಭ್ಯವಿಲ್ಲ. ಕೆಳಗಿನ ಸಂದೇಶವನ್ನು ಓದಿ.",
    unavailable: "ಸೇವೆ ಈಗ ಲಭ್ಯವಿಲ್ಲ. ನಂತರ ಪ್ರಯತ್ನಿಸಿ.",
    recording: "ಕೇಳುತ್ತಿದ್ದೇನೆ…", processing: "ನಿಮ್ಮ ಉತ್ತರವನ್ನು ನೋಡುತ್ತಿದ್ದೇನೆ…", finalKicker: "ಮುಂದಿನ ಹಂತ",
    finalTitle: "ಇವುಗಳನ್ನು ಜೊತೆಗೆ ತೆಗೆದುಕೊಂಡು ಹೋಗಿ", replay: "ಮತ್ತೆ ಪ್ರಾರಂಭಿಸಿ",
    firstQuestion: "ನೀವು ಮಹಿಳೆಯೇ?", languageGroup: "ಭಾಷೆ ಆಯ್ಕೆಮಾಡಿ", conversationLabel: "ಸಂಭಾಷಣೆ",
    documentList: "ದಾಖಲೆಗಳ ಪಟ್ಟಿ", yes: "ಹೌದು", no: "ಇಲ್ಲ", yesAnswer: "ಹೌದು", noAnswer: "ಇಲ್ಲ",
    spokenAnswer: "ನಾನು ಮಾತನಾಡಿ ಉತ್ತರಿಸಿದೆ.", progress: "ಪ್ರಶ್ನೆ", repeatMessage: "ಈ ಸಂದೇಶವನ್ನು ಮತ್ತೆ ಕೇಳಿ",
    thinking: "ಯೋಚಿಸುತ್ತಿದ್ದೇನೆ…", speaking: "ಮಾತನಾಡುತ್ತಿದ್ದೇನೆ…",
    documents: ["ಕೆವೈಸಿ ಅರ್ಜಿ ನಮೂನೆ", "ಅರ್ಜಿದಾರರ ಆಧಾರ್ ಪ್ರತಿ", "ಆಧಾರ್‌ನ ವಿಳಾಸ ಬೇರೆ ಇದ್ದರೆ ವಿಳಾಸದ ಪುರಾವೆ", "ರಾಜ್ಯದ ಪಡಿತರ ಚೀಟಿ ಅಥವಾ ಕುಟುಂಬದ ಸರ್ಕಾರಿ ದಾಖಲೆ", "ಆ ದಾಖಲೆಯಲ್ಲಿರುವ ವಯಸ್ಕರ ಆಧಾರ್ ಪ್ರತಿಗಳು", "ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಪ್ರತಿ ಅಥವಾ ರದ್ದುಪಡಿಸಿದ ಚೆಕ್", "ವಂಚಿತ ಸ್ಥಿತಿಯ ಘೋಷಣೆ"]
  }
};

const languageButtons = [...document.querySelectorAll("[data-language]")];
const welcomeScreen = document.getElementById("welcome-screen");
const guideScreen = document.getElementById("guide-screen");
const finalScreen = document.getElementById("final-screen");
const startButton = document.getElementById("start-button");
const micButton = document.getElementById("mic-button");
const textForm = document.getElementById("text-form");
const textInput = document.getElementById("text-input");
const conversation = document.getElementById("conversation");
const progressIndicator = document.getElementById("progress-indicator");
const yesNoControls = document.getElementById("yes-no-controls");
const yesButton = document.getElementById("yes-button");
const noButton = document.getElementById("no-button");
const voiceStatusText = document.getElementById("voice-status-text");
const statusActivityIcon = document.getElementById("status-activity-icon");
const speakerOffIcon = document.getElementById("speaker-off-icon");
const documentChecklist = document.getElementById("document-checklist");
const questionIds = ["applicant_is_woman", "applicant_age", "poor_household", "household_has_lpg"];

let language = "hi-IN";
let state = { answers: {}, step: 0, recent_turns: [] };
let currentQuestionText = "";
let currentQuestionId = "applicant_is_woman";
let currentQuestionType = "yes_no";
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
let cachedVoices = null;
let voiceListPromise = null;
let currentAudio = null;
let currentAudioUrl = null;
let speechRequestId = 0;
let currentSpeechCacheKey = null;
const fixedSpeechKeys = new Set([
  "greeting",
  "applicant_is_woman",
  "applicant_age",
  "poor_household",
  "household_has_lpg"
]);
const fixedSpeechAudioCache = new Map();

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
  document.getElementById("yes-label").textContent = text.yes;
  document.getElementById("no-label").textContent = text.no;
  document.getElementById("language-list").setAttribute("aria-label", text.languageGroup);
  conversation.setAttribute("aria-label", text.conversationLabel);
  documentChecklist.setAttribute("aria-label", text.documentList);
  yesButton.setAttribute("aria-label", text.yes);
  noButton.setAttribute("aria-label", text.no);
  for (const id of ["welcome-title", "start-label", "caption-heading", "conversation", "voice-status", "mic-label", "text-label", "text-input", "send-button", "yes-label", "no-label", "final-kicker", "final-heading", "final-caption", "document-checklist", "replay-button"]) {
    const el = document.getElementById(id);
    if (el) el.setAttribute("lang", language);
  }
  micButton.setAttribute("aria-label", recorder?.state === "recording" ? text.stop : text.mic);
  startButton.setAttribute("aria-label", text.start);
  textInput.setAttribute("aria-label", text.textLabel);
  document.getElementById("send-button").setAttribute("aria-label", text.send);
  document.querySelectorAll(".repeat-message-button").forEach((btn) => {
    btn.setAttribute("aria-label", text.repeatMessage);
  });
  for (const button of languageButtons) {
    const selected = button.dataset.language === language;
    button.setAttribute("aria-pressed", String(selected));
    button.classList.toggle("is-selected", selected);
  }
  updateProgress(state.step);
}

function setCaption(text, cacheKey = null) {
  currentQuestionText = text;
  currentSpeechCacheKey = cacheKey;
  appendChatMessage("assistant", text, cacheKey);
}

function appendChatMessage(role, text, cacheKey = null) {
  const bubble = document.createElement("article");
  bubble.className = `chat-message chat-${role}`;
  bubble.lang = language;
  const content = document.createElement("p");
  content.className = "chat-message-text";
  content.textContent = text;
  bubble.append(content);
  if (role === "assistant") {
    const repeatButton = document.createElement("button");
    repeatButton.type = "button";
    repeatButton.className = "repeat-message-button";
    repeatButton.setAttribute("aria-label", words().repeatMessage);
    repeatButton.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 9v6h4l5 4V5L8 9H4zM17 9a5 5 0 0 1 0 6m2-9a9 9 0 0 1 0 12"/></svg>';
    repeatButton.addEventListener("click", () => void speak(text, cacheKey));
    bubble.append(repeatButton);
  }
  conversation.append(bubble);
  conversation.scrollTop = conversation.scrollHeight;
}

function updateProgress(step) {
  progressIndicator.replaceChildren();
  questionIds.forEach((questionId, index) => {
    const dot = document.createElement("span");
    dot.className = "progress-dot";
    const isFilled = step >= questionIds.length ? true : index <= step;
    dot.classList.toggle("is-filled", isFilled);
    dot.setAttribute("aria-hidden", "true");
    progressIndicator.append(dot);
  });
  const currentStepNum = Math.min(step + 1, questionIds.length);
  const progressText = `${words().progress} ${currentStepNum} / ${questionIds.length}`;
  progressIndicator.setAttribute("aria-label", progressText);
}

function setCurrentQuestion(questionId, questionType, step) {
  currentQuestionId = questionId;
  currentQuestionType = questionType;
  yesNoControls.hidden = questionType !== "yes_no";
  updateProgress(step);
}

function setVoiceStatus(text, speakerUnavailable = false) {
  voiceStatusText.textContent = text;
  speakerOffIcon.toggleAttribute("hidden", !speakerUnavailable);
  statusActivityIcon.toggleAttribute("hidden", !text || speakerUnavailable);
}

function setSubmitting(submitting) {
  waitingForTurn = submitting;
  micButton.disabled = submitting;
  textInput.disabled = submitting;
  document.getElementById("send-button").disabled = submitting;
  yesButton.disabled = submitting;
  noButton.disabled = submitting;
}

function waitForVoices() {
  const synthesis = window.speechSynthesis;
  if (!synthesis) return Promise.resolve([]);
  if (cachedVoices?.length) return Promise.resolve(cachedVoices);
  if (voiceListPromise) return voiceListPromise;

  voiceListPromise = new Promise((resolve) => {
    let settled = false;
    const finish = (voices) => {
      if (settled) return;
      settled = true;
      cachedVoices = voices;
      resolve(voices);
      if (voices.length) {
        synthesis.removeEventListener("voiceschanged", handleVoicesChanged);
      }
    };
    const handleVoicesChanged = () => {
      const voices = synthesis.getVoices();
      if (voices.length) finish(voices);
    };

    synthesis.addEventListener("voiceschanged", handleVoicesChanged);
    window.setTimeout(() => finish(synthesis.getVoices()), 650);
  });
  return voiceListPromise;
}

function findVoice(voices, locale) {
  const normalized = locale.toLowerCase();
  const exactVoice = voices.find((voice) => voice.lang.toLowerCase() === normalized);
  if (exactVoice) return exactVoice;
  const languagePrefix = normalized.split("-")[0];
  return voices.find((voice) => voice.lang.toLowerCase().split("-")[0] === languagePrefix);
}

function stopCurrentAudio() {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio.src = "";
    currentAudio = null;
  }
  if (currentAudioUrl) URL.revokeObjectURL(currentAudioUrl);
  currentAudioUrl = null;
}

function playAudio(blob) {
  return new Promise((resolve, reject) => {
    const objectUrl = URL.createObjectURL(blob);
    const audio = new Audio(objectUrl);
    currentAudio = audio;
    currentAudioUrl = objectUrl;
    setVoiceStatus(words().speaking);
    const finish = (error = null) => {
      if (currentAudio === audio) currentAudio = null;
      if (currentAudioUrl === objectUrl) currentAudioUrl = null;
      URL.revokeObjectURL(objectUrl);
      setVoiceStatus("");
      if (error) reject(error);
      else resolve();
    };
    audio.addEventListener("ended", () => finish(), { once: true });
    audio.addEventListener("error", () => finish(new Error("Audio playback failed.")), { once: true });
    audio.play().catch(finish);
  });
}

async function requestSpeechAudio(text, cacheKey, requestId) {
  const cacheId = fixedSpeechKeys.has(cacheKey)
    ? `${language}:${cacheKey}:${text}`
    : null;
  let audioBlob = cacheId ? fixedSpeechAudioCache.get(cacheId) : null;
  if (!audioBlob) {
    const response = await fetch("/api/speak", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, lang: language })
    });
    if (!response.ok) throw new Error("Speech service unavailable.");
    audioBlob = await response.blob();
    if (cacheId) fixedSpeechAudioCache.set(cacheId, audioBlob);
  }
  if (requestId !== speechRequestId) return;
  await playAudio(audioBlob);
}

async function speak(text, cacheKey = null, { preserveStatus = false } = {}) {
  const requestId = ++speechRequestId;
  window.speechSynthesis?.cancel();
  stopCurrentAudio();

  const utterance = window.SpeechSynthesisUtterance
    ? new SpeechSynthesisUtterance(text)
    : null;
  if (utterance) utterance.lang = language;

  const voices = await waitForVoices();
  if (requestId !== speechRequestId) return false;
  const voice = findVoice(voices, language);
  if (voice && utterance && window.speechSynthesis) {
    utterance.voice = voice;
    utterance.rate = 0.88;
    setVoiceStatus(words().speaking);
    return new Promise((resolve) => {
      utterance.onend = () => {
        setVoiceStatus("");
        resolve(true);
      };
      utterance.onerror = () => {
        setVoiceStatus(words().noVoice, true);
        resolve(false);
      };
      window.speechSynthesis.speak(utterance);
    });
  }

  const previousStatus = preserveStatus ? voiceStatusText.textContent : "";
  setVoiceStatus([previousStatus, words().noVoice].filter(Boolean).join(" "), true);
  try {
    await requestSpeechAudio(text, cacheKey, requestId);
    return true;
  } catch {
    return false;
  }
}

function showTextFallback(message) {
  fallbackEnabled = true;
  textForm.hidden = false;
  appendChatMessage("assistant", message);
  setVoiceStatus(message);
  textInput.focus();
  void speak(message, null, { preserveStatus: true });
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

async function sendTurn({ text = null, blob = null, displayText = null } = {}) {
  if (waitingForTurn) return;
  setSubmitting(true);
  setVoiceStatus(words().thinking);
  appendChatMessage("user", displayText || text || words().spokenAnswer);
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
    const result = await response.json();
    language = result.lang || language;
    state = result.state || state;
    updateLanguage(language);
    silenceCount = 0;
    if (!response.ok || result.error_code) {
      setCaption(result.reply_text || words().unavailable);
      setVoiceStatus("");
      void speak(result.reply_text || words().unavailable);
      return;
    }
    if (!result.done && result.question_id) {
      setCurrentQuestion(result.question_id, result.question_type, state.step);
    } else {
      yesNoControls.hidden = true;
      updateProgress(questionIds.length);
    }
    setCaption(result.reply_text, result.speech_cache_key);
    setVoiceStatus("");
    if (result.done) {
      document.getElementById("final-caption").textContent = result.reply_text;
      document.getElementById("final-caption").lang = language;
      renderChecklist(result.checklist);
      guideScreen.hidden = true;
      finalScreen.hidden = false;
    }
    void speak(result.reply_text, result.speech_cache_key);
  } catch {
    const fallback = words().unavailable;
    appendChatMessage("assistant", fallback);
    setVoiceStatus(fallback);
    void speak(fallback);
  } finally {
    setSubmitting(false);
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
          setVoiceStatus(words().repeat);
          void speak(currentQuestionText, currentSpeechCacheKey, { preserveStatus: true });
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
    setVoiceStatus(words().recording);
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
  state = { answers: {}, step: 0, recent_turns: [] };
  currentQuestionId = questionIds[0];
  currentQuestionType = "yes_no";
  silenceCount = 0;
  fallbackEnabled = false;
  setVoiceStatus("");
  textForm.hidden = false;
  conversation.replaceChildren();
  setCurrentQuestion(currentQuestionId, currentQuestionType, 0);
  welcomeScreen.hidden = true;
  finalScreen.hidden = true;
  guideScreen.hidden = false;
  const greeting = words().greeting;
  setCaption(greeting, "greeting");
  void speak(greeting, "greeting").then(() => {
    if (guideScreen.hidden) return;
    const firstQuestion = words().firstQuestion;
    setCaption(firstQuestion, "applicant_is_woman");
    void speak(firstQuestion, "applicant_is_woman");
  });
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
yesButton.addEventListener("click", () => {
  void sendTurn({ text: words().yesAnswer, displayText: words().yes });
});
noButton.addEventListener("click", () => {
  void sendTurn({ text: words().noAnswer, displayText: words().no });
});
document.getElementById("replay-button").addEventListener("click", startFlow);

updateLanguage(language);
void waitForVoices();