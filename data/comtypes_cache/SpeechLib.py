from enum import IntEnum, IntFlag

import comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 as __wrapper_module__
from comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 import (
    SECFEmulateResult, SPPHRASE, eLEXTYPE_PRIVATE13,
    DISPID_SPPFirstElement, ISpeechPhraseProperties, SVSFParseSsml,
    SPFM_CREATE, eLEXTYPE_PRIVATE5, DISPID_SCSBaseStream,
    ISpeechLexiconPronunciation, SpInprocRecognizer, SP_VISEME_1,
    DISPID_SOTs_NewEnum, SAFTADPCM_22kHzMono, DISPID_SGRSTPropertyId,
    SAFT44kHz8BitStereo, eLEXTYPE_RESERVED8, ISpRecoResult,
    SVEVoiceChange, DISPID_SBSWrite, DISPID_SOTRemove,
    DISPID_SGRSRule, SDTAll, SRSInactive, SpeechCategoryAppLexicons,
    SVP_8, SRESoundStart, DISPID_SLPPartOfSpeech,
    DISPID_SRCCreateGrammar, SPINTERFERENCE_NONE,
    DISPID_SGRInitialState, SPVOICESTATUS, SPXRO_SML, SFTSREngine,
    DISPID_SVSpeakCompleteEvent, DISPID_SVEventInterests,
    STCInprocServer, DISPID_SMSADeviceId, SRTReSent,
    eLEXTYPE_RESERVED6, SAFTCCITT_uLaw_11kHzStereo, DISPID_SPCLangId,
    SVP_7, DISPID_SPIEnginePrivateData, SPEI_START_SR_STREAM,
    ISpStreamFormat, SGSDisabled, SPINTERFERENCE_TOOLOUD,
    ISpeechPhraseElements, DISPID_SRRGetXMLErrorInfo, SITooQuiet,
    SP_VISEME_6, Speech_StreamPos_Asap, DISPID_SABufferNotifySize,
    SAFT12kHz8BitStereo, DISPID_SMSALineId, dispid,
    SAFTGSM610_8kHzMono, SVSFUnusedFlags, SPWORD, ISpPhoneConverter,
    SVP_20, SVP_10, ISpeechGrammarRules, DISPID_SPPName,
    DISPID_SVSInputSentencePosition, ISpEventSource, DISPID_SVSpeak,
    DISPID_SPAPhraseInfo, SPRS_ACTIVE, SpeechCategoryAudioOut,
    STSF_FlagCreate, SGRSTTRule, SPEI_SR_BOOKMARK, SLTApp,
    DISPID_SPEEngineConfidence, SDKLCurrentUser, eLEXTYPE_PRIVATE1,
    SVPOver, DISPID_SBSFormat, DISPID_SRGDictationUnload,
    SAFT22kHz16BitStereo, SPEI_SR_PRIVATE, SPPHRASEELEMENT,
    SpeechPropertyNormalConfidenceThreshold,
    DISPID_SRGetPropertyNumber, eLEXTYPE_PRIVATE14, SPEI_UNDEFINED,
    SREAudioLevel, DISPID_SASState, SWPUnknownWordPronounceable,
    SpeechAudioFormatGUIDWave, SAFT24kHz8BitMono, SRTAutopause, SVP_9,
    DISPID_SLRemovePronunciation, SPEI_HYPOTHESIS, DISPID_SRGCommit,
    SVSFPurgeBeforeSpeak, DISPID_SABIEventBias, SPDKL_LocalMachine,
    SDA_Consume_Leading_Spaces, SREAdaptation, DISPID_SRGState,
    DISPID_SPEActualConfidence, DISPID_SGRsCommit, SRATopLevel,
    SECFNoSpecialChars, ISpObjectTokenCategory, SREPhraseStart,
    DISPID_SRGCmdSetRuleIdState, ISpeechRecognizerStatus,
    DISPID_SADefaultFormat, DISPID_SPRuleFirstElement,
    DISPID_SRGetRecognizers, SAFTCCITT_uLaw_44kHzStereo,
    DISPID_SRGCmdLoadFromObject, DISPID_SAEventHandle,
    SSSPTRelativeToStart, tagSTATSTG, SPRS_ACTIVE_WITH_AUTO_PAUSE,
    eLEXTYPE_PRIVATE2, SWPUnknownWordUnpronounceable, SpStream,
    DISPID_SRCEPropertyStringChange, SP_VISEME_20, DISPID_SPPValue,
    DISPID_SABIMinNotification, SVSFParseAutodetect,
    SPINTERFERENCE_LATENCY_TRUNCATE_END, DISPID_SRSAudioStatus,
    DISPID_SRIsUISupported, IServiceProvider, DISPID_SVVoice,
    DISPID_SRCERecognizerStateChange, SSSPTRelativeToCurrentPosition,
    SpeechAudioFormatGUIDText, SPCT_SUB_DICTATION,
    SAFT11kHz8BitStereo, SPEI_MAX_SR, DISPID_SRCVoicePurgeEvent,
    DISPID_SLGetGenerationChange, SPSVerb, SPGS_ENABLED,
    SAFTADPCM_44kHzMono, ISpPhrase, DISPID_SPARecoResult,
    IInternetSecurityMgrSite, SAFT11kHz16BitMono,
    DISPID_SRCCmdMaxAlternates, SPEI_TTS_BOOKMARK,
    SAFT48kHz16BitStereo, SDKLCurrentConfig, SVEEndInputStream,
    DISPID_SOTsItem, DISPID_SDKSetBinaryValue, SPDKL_CurrentConfig,
    ISpResourceManager, SAFTCCITT_uLaw_8kHzMono,
    eLEXTYPE_VENDORLEXICON, SASPause, SVF_None, SpMemoryStream,
    ISequentialStream, ISpProperties, eLEXTYPE_LETTERTOSOUND,
    DISPID_SRState, SPFM_NUM_MODES, SDKLLocalMachine,
    DISPID_SPIElements, DISPID_SRCRetainedAudioFormat, SPEI_PHONEME,
    SPCS_ENABLED, DISPID_SRGDictationSetState,
    DISPID_SRCEPropertyNumberChange, DISPID_SRCEHypothesis, SVP_1,
    DISPID_SVEVoiceChange, SPAUDIOBUFFERINFO, SAFT12kHz16BitStereo,
    IEnumString, SPSEMANTICERRORINFO, SRARoot, SP_VISEME_11,
    SPLO_STATIC, DISPID_SVSLastBookmarkId, SREStreamEnd,
    ISpeechObjectTokens, SPCT_DICTATION, DISPID_SRGCmdLoadFromMemory,
    DISPID_SLGetPronunciations, SASClosed, SSTTWildcard,
    SPWP_KNOWN_WORD_PRONOUNCEABLE, SVEWordBoundary, Library,
    SPPHRASEREPLACEMENT, SVSFIsNotXML, DISPID_SASetState, SAFTDefault,
    DISPID_SABIBufferSize, WSTRING, UINT_PTR, eLEXTYPE_PRIVATE10,
    DISPID_SRSClsidEngine, SVEBookmark, SGRSTTEpsilon, SpShortcut,
    SRADynamic, DISPID_SDKGetStringValue, SRAImport,
    eLEXTYPE_PRIVATE8, DISPID_SVESentenceBoundary,
    SAFT24kHz8BitStereo, tagSPPROPERTYINFO,
    ISpeechGrammarRuleStateTransition, eWORDTYPE_ADDED, SPRULE,
    SpeechCategoryRecoProfiles, SVSFParseMask, ISpPhraseAlt, ISpVoice,
    SPSNotOverriden, DISPID_SAFSetWaveFormatEx,
    DISPID_SPERetainedSizeBytes, COMMETHOD, eLEXTYPE_PRIVATE15,
    SECNormalConfidence, SSFMOpenReadWrite, DISPID_SRGCmdLoadFromFile,
    DISPID_SPILanguageId, ISpeechPhraseInfoBuilder,
    DISPID_SOTCDefault, SAFTCCITT_ALaw_22kHzMono,
    SDA_One_Trailing_Space, DISPID_SLRemovePronunciationByPhoneIds,
    eLEXTYPE_MORPHOLOGY, _ISpeechVoiceEvents, DISPID_SPIStartTime,
    SVP_12, ISpeechRecognizer, SPEI_RESERVED6,
    DISPID_SWFEAvgBytesPerSec, SAFT16kHz16BitMono,
    DISPID_SPISaveToMemory, SPSHT_Unknown, DISPID_SPIRule, GUID,
    SPSMF_UPS, SWTAdded, SP_VISEME_13, DISPID_SRCEPhraseStart,
    ISpGrammarBuilder, ISpeechRecoResultDispatch, DISPID_SPRulesCount,
    SPSHT_NotOverriden, SSTTTextBuffer, SPEI_MAX_TTS, ISpStream,
    ISpeechBaseStream, SAFT12kHz16BitMono, IStream,
    SPSHORTCUTPAIRLIST, DISPID_SDKEnumValues,
    DISPID_SASCurrentDevicePosition, ISpeechObjectToken,
    DISPID_SVAudioOutput, SASStop, IInternetSecurityManager, SINoise,
    DISPID_SRCBookmark, SAFT12kHz8BitMono, SDTLexicalForm,
    DISPID_SVSLastBookmark, SAFT8kHz16BitMono, SAFT32kHz16BitMono,
    SVSFIsFilename, SASRun, DISPID_SRCCreateResultFromMemory,
    SPWT_LEXICAL, SFTInput, SPBO_TIME_UNITS, SPVPRI_ALERT,
    DISPID_SASCurrentSeekPosition, DISPID_SLPType, SGRSTTWildcard,
    SpCompressedLexicon, DISPID_SRSCurrentStreamNumber, SPWF_SRENGINE,
    DISPID_SVEViseme, SRSInactiveWithPurge, SRSEDone, DISPID_SGRsItem,
    SpeechPropertyResponseSpeed, ISpeechXMLRecoResult,
    DISPID_SVEStreamStart, SDTAudio, SpObjectToken, SVSFVoiceMask,
    eLEXTYPE_PRIVATE18, SPSHT_OTHER, _LARGE_INTEGER, DISPID_SVEWord,
    DISPID_SPANumberOfElementsInResult,
    DISPID_SPIGetDisplayAttributes, ISpeechPhraseReplacement,
    SAFTCCITT_uLaw_44kHzMono, SpeechRegistryLocalMachineRoot,
    SPWT_LEXICAL_NO_SPECIAL_CHARS, SSSPTRelativeToEnd, ISpShortcut,
    DISPID_SRGId, DISPID_SGRSAddWordTransition, SpMMAudioEnum,
    SVEStartInputStream, SpeechTokenValueCLSID, SP_VISEME_5,
    DISPID_SVStatus, ISpRecoGrammar2, ISpeechObjectTokenCategory,
    SVP_18, SPWF_INPUT, DISPID_SRRDiscardResultInfo,
    SPINTERFERENCE_TOOQUIET, DISPID_SOTRemoveStorageFileName,
    SpeechRegistryUserRoot, DISPID_SPPs_NewEnum,
    SGLexicalNoSpecialChars, ISpeechAudioFormat, SPWORDLIST,
    DISPID_SMSGetData, DISPID_SRDisplayUI, DISPID_SWFEChannels,
    SAFTCCITT_ALaw_44kHzStereo, DISPID_SLAddPronunciation,
    DISPID_SOTIsUISupported, DISPID_SGRsDynamic,
    DISPID_SPPBRestorePhraseFromMemory,
    ISpeechTextSelectionInformation, ISpeechPhraseElement,
    eLEXTYPE_PRIVATE17, ISpNotifyTranslator, CoClass, SP_VISEME_4,
    SpeechAllElements, DISPID_SLWs_NewEnum, SVP_0, DISPID_SRGRules,
    SAFT44kHz16BitMono, SpSharedRecognizer, SRCS_Disabled,
    SGDSInactive, DISPID_SPRText, DISPID_SPELexicalForm,
    SpeechDictationTopicSpelling, DISPID_SRGSetTextSelection,
    DISPID_SPACommit, SP_VISEME_7, DISPID_SREmulateRecognition,
    SPAUDIOSTATUS, SAFT24kHz16BitMono, SAFTADPCM_8kHzMono,
    Speech_Default_Weight, STSF_CommonAppData, SVEPrivate,
    DISPID_SGRSTType, SpInProcRecoContext, tagSPTEXTSELECTIONINFO,
    DISPID_SOTsCount, SAFTNoAssignedFormat, SPEI_SR_AUDIO_LEVEL,
    SAFTCCITT_ALaw_11kHzStereo, SpeechCategoryVoices,
    DISPID_SPRNumberOfElements, DISPID_SRCreateRecoContext,
    SPWORDPRONUNCIATIONLIST, ISpeechMemoryStream, eLEXTYPE_PRIVATE12,
    ISpRecognizer, SVSFDefault, SDTReplacement,
    DISPID_SRGetPropertyString, DISPID_SLWPronunciations, SPAR_Medium,
    DISPID_SRRTTickCount, SPCT_COMMAND, SAFT8kHz8BitStereo,
    ISpeechRecoContext, DISPID_SOTDisplayUI, ISpeechPhraseInfo,
    SRAExport, SPAO_RETAIN_AUDIO, SITooFast, SPEI_MIN_SR,
    ISpeechPhraseRule, STSF_AppData, SVSFNLPMask,
    ISpeechPhraseProperty, DISPID_SPERequiredConfidence,
    SPVPRI_NORMAL, ISpeechPhraseAlternate, SRSActive,
    ISpeechVoiceStatus, SLODynamic, DISPID_SRCEEndStream,
    DISPID_SDKDeleteValue, DISPID_SPRs_NewEnum, DISPID_SLPs_NewEnum,
    DISPID_SPERetainedStreamOffset, SPPS_Noun, DISPID_SRAudioInput,
    DISPID_SRSSupportedLanguages, DISPID_SVSyncronousSpeakTimeout,
    ISpeechRecoGrammar, DISPID_SRRTLength, SPRS_ACTIVE_USER_DELIMITED,
    DISPID_SPIRetainedSizeBytes, _check_version, SVEAudioLevel,
    STSF_LocalAppData, DISPID_SVPriority, SpNullPhoneConverter,
    SPBO_NONE, SpMMAudioOut, ISpeechGrammarRule, DISPID_SDKDeleteKey,
    DISPID_SRCEAdaptation, DISPID_SPPEngineConfidence,
    eLEXTYPE_PRIVATE16, SPRST_ACTIVE_ALWAYS, DISPID_SPIAudioSizeBytes,
    SVP_16, SGDSActiveUserDelimited, SPRECORESULTTIMES,
    DISPID_SAFGetWaveFormatEx, DISPID_SGRClear,
    DISPID_SRRTOffsetFromStart, SpeechPropertyResourceUsage, SVP_11,
    DISPID_SPRulesItem, SPEI_RECOGNITION, DISPID_SABufferInfo,
    SAFT22kHz8BitStereo, SAFTADPCM_22kHzStereo, ISpeechVoice,
    SAFT16kHz16BitStereo, ISpEventSink, SpeechCategoryRecognizers,
    SVPAlert, DISPID_SVGetAudioOutputs, SPEI_PHRASE_START,
    SSTTDictation, SpUnCompressedLexicon, SPPROPERTYINFO,
    eLEXTYPE_PRIVATE11, SAFTADPCM_8kHzStereo, DISPID_SGRSTWeight,
    DISPID_SVAlertBoundary, DISPID_SRAudioInputStream,
    DISPID_SRCRequestedUIType, Speech_StreamPos_RealTime,
    SpFileStream, SRERequestUI, DISPID_SRCPause,
    DISPID_SPEPronunciation, DISPID_SWFESamplesPerSec,
    DISPID_SRRSpeakAudio, SRSEIsSpeaking, SPEI_RESERVED3,
    ISpeechDataKey, SPEI_RESERVED2, SPRST_INACTIVE_WITH_PURGE,
    SPEI_TTS_AUDIO_LEVEL, DISPID_SDKOpenKey, SPPS_Unknown, SPSLMA,
    SPPS_Function, __MIDL___MIDL_itf_sapi_0000_0020_0002, STCAll,
    SBONone, SGDSActive, eWORDTYPE_DELETED,
    DISPID_SRSetPropertyString, SECFIgnoreWidth,
    SPEI_PROPERTY_NUM_CHANGE, SRADefaultToActive, DISPID_SLPsCount,
    ISpeechResourceLoader, SpeechTokenKeyUI, DISPID_SRStatus,
    DISPID_SRGIsPronounceable, DISPID_SRRGetXMLResult,
    ISpeechLexiconWords, SpeechAudioProperties,
    DISPID_SRGCmdLoadFromProprietaryGrammar, SpPhoneConverter,
    DISPID_SRRPhraseInfo, DISPID_SOTCreateInstance, SREBookmark,
    SAFTCCITT_uLaw_22kHzStereo, DISPID_SRRSetTextFeedback,
    SPCS_DISABLED, DISPID_SRSCurrentStreamPosition, ISpRecoGrammar,
    SGLexical, SpMMAudioIn, ISpRecoContext2, SPPS_RESERVED2,
    ISpNotifySource, ISpMMSysAudio, SVP_21, SpeechTokenKeyFiles,
    SRTEmulated, eLEXTYPE_PRIVATE20, SP_VISEME_17, SPPS_RESERVED3,
    VARIANT, SP_VISEME_18, SVP_17, SpTextSelectionInformation,
    DISPID_SGRSTPropertyName, SpeechCategoryPhoneConverters,
    DISPID_SOTId, SVF_Stressed, DISPID_SPEsCount, ISpeechCustomStream,
    Speech_Max_Word_Length, DISPID_SPEAudioSizeTime,
    DISPID_SRIsShared, DISPID_SPPChildren, DISPID_SWFEExtraData,
    DISPID_SGRSTPropertyValue, ISpLexicon, SVP_2, DISPID_SRGetFormat,
    __MIDL_IWinTypes_0009, SAFTGSM610_11kHzMono, DISPID_SBSRead,
    DISPID_SRRTimes, BSTR, SREStateChange, DISPID_SGRAttributes,
    __MIDL___MIDL_itf_sapi_0000_0020_0001, SGRSTTTextBuffer,
    DISPID_SVSpeakStream, SGSEnabled, DISPID_SPEs_NewEnum,
    DISPID_SOTCSetId, SPEI_END_SR_STREAM, SRTSMLTimeout,
    ISpeechRecoResult, DISPID_SVEEnginePrivate, ISpeechPhraseRules,
    SPEI_INTERFERENCE, eLEXTYPE_PRIVATE19, SPCT_SUB_COMMAND,
    DISPID_SPRuleChildren, DISPID_SPRFirstElement,
    DISPID_SVSInputWordLength, SPSMF_SRGS_SAPIPROPERTIES,
    ISpeechPhraseAlternates, DISPID_SOTCGetDataKey,
    SPINTERFERENCE_LATENCY_WARNING, ISpRecoContext, SSFMOpenForRead,
    SpeechPropertyAdaptationOn, SpeechCategoryAudioIn,
    SAFT24kHz16BitStereo, DISPID_SRCERecognitionForOtherContext,
    SpeechPropertyLowConfidenceThreshold, ISpeechFileStream, SVP_3,
    ISpeechLexiconPronunciations, SREPropertyNumChange, SP_VISEME_16,
    DISPID_SASNonBlockingIO, SpeechTokenIdUserLexicon,
    ISpSerializeState, DISPID_SRAllowVoiceFormatMatchingOnNextSet,
    ISpeechAudioBufferInfo, SPWP_UNKNOWN_WORD_PRONOUNCEABLE,
    DISPID_SGRSTText, SVSFParseSapi, SpeechTokenKeyAttributes,
    SRAInterpreter, SAFTADPCM_44kHzStereo, SPEI_RESERVED5,
    SAFT44kHz8BitMono, SDTPronunciation, eLEXTYPE_PRIVATE4,
    SPEI_ADAPTATION, SPSModifier, SECLowConfidence,
    DISPID_SLPPhoneIds, SPEI_REQUEST_UI, DISPID_SGRAddResource,
    DISPID_SAFType, DISPID_SRCSetAdaptationData, SAFT48kHz8BitStereo,
    ISpPhoneticAlphabetSelection, SITooLoud, DISPID_SLPsItem,
    SpPhoneticAlphabetConverter, DISPID_SPRsCount, STCInprocHandler,
    ISpObjectWithToken, LONG_PTR, SPEI_START_INPUT_STREAM,
    SAFT11kHz8BitMono, SPAS_STOP, DISPID_SVAudioOutputStream,
    SAFT48kHz8BitMono, ISpeechAudioStatus, SpeechUserTraining,
    SGRSTTWord, STCLocalServer, DISPID_SDKGetlongValue,
    eLEXTYPE_PRIVATE3, SPPS_Verb, DISPID_SVResume, DISPID_SGRsCount,
    DISPID_SPEAudioStreamOffset, SVEPhoneme, DISPID_SPPParent,
    SVSFlagsAsync, DISPID_SDKGetBinaryValue, DISPID_SOTGetAttribute,
    DISPID_SRCEAudioLevel, SVP_6, SAFTADPCM_11kHzMono,
    DISPID_SWFEFormatTag, DISPID_SVEPhoneme, SAFT8kHz8BitMono,
    SPEI_TTS_PRIVATE, DISPID_SGRId, DISPID_SRRAudio,
    DISPID_SPEAudioSizeBytes, ULONG_PTR, DISPID_SPEDisplayAttributes,
    typelib_path, DISPID_SOTSetId, SGDisplay, DISPID_SGRs_NewEnum,
    SPBO_AHEAD, DISPID_SRCEStartStream,
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C, DISPID_SPAs_NewEnum,
    SPEI_END_INPUT_STREAM, SAFT22kHz8BitMono,
    ISpPhoneticAlphabetConverter, DISPID_SDKCreateKey, SPVPRI_OVER,
    ISpStreamFormatConverter, SPXRO_Alternates_SML,
    DISPID_SGRSTransitions, DISPID_SGRsAdd, ISpObjectToken,
    DISPMETHOD, DISPID_SAVolume, DISPID_SRSNumberOfActiveRules,
    eLEXTYPE_RESERVED9, SECFIgnoreCase, SpSharedRecoContext, SAFTText,
    SREPrivate, DISPID_SPEsItem, SP_VISEME_9, SSFMCreate,
    SAFTCCITT_uLaw_8kHzStereo, SPAS_CLOSED, DISPID_SVSPhonemeId,
    DISPID_SPRuleEngineConfidence, DISPID_SRGReset,
    SPEI_SENTENCE_BOUNDARY, SpPhraseInfoBuilder,
    SpeechVoiceSkipTypeSentence, SREInterference,
    DISPID_SDKSetLongValue, DISPID_SMSSetData, SPSMF_SAPI_PROPERTIES,
    DISPID_SRGRecoContext, DISPID_SRCRetainedAudio,
    SDKLDefaultLocation, DISPID_SPIEngineId,
    SAFTCCITT_ALaw_22kHzStereo, DISPID_SLWWord, SAFT32kHz16BitStereo,
    SPEI_ACTIVE_CATEGORY_CHANGED, SPEI_RECO_STATE_CHANGE,
    DISPID_SFSOpen, DISPID_SVSkip, SPAS_PAUSE, SRERecoOtherContext,
    ISpeechPhoneConverter, SPSNoun, SPWORDPRONUNCIATION,
    DISPID_SAStatus, SREAllEvents, DISPID_SVEAudioLevel,
    DISPID_SRCEInterference, DISPID_SRCESoundStart,
    ISpeechRecoResultTimes, ISpeechRecoResult2,
    SPINTERFERENCE_NOSIGNAL, SVP_19, ISpRecognizer3, DISPID_SVRate,
    DISPID_SRCESoundEnd, SVP_5, DISPID_SLWsItem,
    DISPID_SRCEEnginePrivate, DISPID_SPCPhoneToId,
    SAFT44kHz16BitStereo, DISPID_SVVolume, DISPID_SLWType,
    DISPID_SPAsCount, SAFT22kHz16BitMono, DISPID_SRCEFalseRecognition,
    DISPID_SVSRunningState, SAFTExtendedAudioFormat, ISpNotifySink,
    SVSFPersistXML, SPINTERFERENCE_TOOFAST, SPEI_SOUND_START,
    SpeechGrammarTagUnlimitedDictation,
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet, wireHWND,
    WAVEFORMATEX, SPRST_NUM_STATES, SPLO_DYNAMIC, SVP_15,
    SRERecognition, DISPID_SOTGetDescription, DISPID_SPRsItem,
    SPRECOCONTEXTSTATUS, DISPID_SGRSTNextState, SAFT32kHz8BitStereo,
    DISPID_SRGCmdLoadFromResource, SAFT16kHz8BitStereo,
    SPEI_FALSE_RECOGNITION, DISPID_SOTCategory, SPAO_NONE,
    DISPID_SRCResume, SDTAlternates, SPEI_MIN_TTS,
    DISPID_SPEAudioTimeOffset, SITooSlow, SLTUser, DISPID_SRCVoice,
    SVP_13, SPBINARYGRAMMAR, DISPID_SGRAddState, DISPID_SPRuleName,
    DISPID_SDKEnumKeys, DISPIDSPTSI_SelectionOffset, SGSExclusive,
    helpstring, SpStreamFormatConverter, SPTEXTSELECTIONINFO,
    SPRST_INACTIVE, DISPID_SLAddPronunciationByPhoneIds, SVF_Emphasis,
    eLEXTYPE_RESERVED10, DISPID_SVIsUISupported, SRTExtendableParse,
    DISPID_SASFreeBufferSpace, eLEXTYPE_APP, SPSFunction, _FILETIME,
    _RemotableHandle, SRAONone, DISPID_SPEDisplayText,
    SAFTNonStandardFormat, SDTRule, SPSInterjection, SPSHT_EMAIL,
    DISPID_SFSClose, SP_VISEME_2, DISPID_SAFGuid, SPAR_Low,
    IEnumSpObjectTokens, SVSFIsXML, SVEViseme,
    SAFTTrueSpeech_8kHz1BitMono, SpResourceManager, SPPS_Noncontent,
    SPEVENT, SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE, SPGS_DISABLED,
    DISPID_SVSInputSentenceLength, SP_VISEME_8, SPEI_VISEME,
    SPDKL_DefaultLocation, SPBO_PAUSE, SVP_4, Speech_Max_Pron_Length,
    SDTProperty, DISPID_SPIAudioStreamPosition,
    SAFTCCITT_ALaw_8kHzStereo, SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN,
    STCRemoteServer, SGDSActiveWithAutoPause, SRCS_Enabled,
    DISPID_SPIProperties, SINone, DISPID_SRRecognizer,
    DISPID_SRCEventInterests, DISPID_SPRuleId, SPSSuppressWord,
    SLOStatic, DISPID_SGRSAddRuleTransition, DISPID_SVWaitUntilDone,
    ISpeechGrammarRuleStateTransitions, ISpeechMMSysAudio,
    SPSERIALIZEDRESULT, SPSHORTCUTPAIR, DISPID_SRCERecognition,
    DISPID_SGRsCommitAndSave, SPPS_NotOverriden, DISPID_SLGetWords,
    ISpeechGrammarRuleState, DISPID_SPAsItem, SPWT_PRONUNCIATION,
    ISpAudio, SpAudioFormat, SPRST_ACTIVE, DISPID_SOTCId,
    eLEXTYPE_USER_SHORTCUT, ISpDataKey, DISPID_SRSetPropertyNumber,
    DISPID_SGRsFindRule, SPPHRASEPROPERTY, SVP_14,
    SAFTCCITT_ALaw_8kHzMono, DISPIDSPTSI_ActiveLength, SpLexicon,
    DISPID_SGRSTsCount, DISPID_SPIGrammarId, DISPID_SRRRecoContext,
    SINoSignal, SpCustomStream, eLEXTYPE_RESERVED4,
    DISPID_SOTCEnumerateTokens, DISPID_SPIAudioSizeTime, SPSUnknown,
    DISPID_SRCRecognizer, DISPID_SRCEBookmark,
    DISPID_SRGDictationLoad, DISPID_SVSLastStreamNumberQueued,
    SAFTCCITT_ALaw_11kHzMono, SpeechGrammarTagWildcard,
    SAFTGSM610_22kHzMono, SPPS_Interjection, eLEXTYPE_PRIVATE6,
    SPGS_EXCLUSIVE, SECHighConfidence, SPSERIALIZEDPHRASE, SBOPause,
    SP_VISEME_10, SP_VISEME_21, DISPID_SRCAudioInInterferenceStatus,
    SPFM_OPEN_READONLY, DISPID_SPAStartElementInResult, SREHypothesis,
    SECFIgnoreKanaType, SAFT16kHz8BitMono, SPFM_CREATE_ALWAYS,
    DISPID_SVEStreamEnd, SpWaveFormatEx, DISPID_SPRuleConfidence,
    DISPID_SLWsCount, SPWT_DISPLAY, DISPID_SRCState, SRESoundEnd,
    _ISpeechRecoContextEvents, SpNotifyTranslator,
    SAFTCCITT_uLaw_11kHzMono, VARIANT_BOOL, SREFalseRecognition,
    ISpRecognizer2, SAFT48kHz16BitMono, DISPID_SVSLastResult,
    DISPID_SGRSAddSpecialTransition, SPPS_RESERVED4, SVSFNLPSpeakPunc,
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS, SVPNormal, SECFDefault,
    DISPID_SPIGetText, SAFT8kHz16BitStereo, SPEI_WORD_BOUNDARY,
    SGPronounciation, SWTDeleted, eLEXTYPE_USER, DISPID_SVDisplayUI,
    SpVoice, SAFT11kHz16BitStereo, SPPS_RESERVED1, SVEAllEvents,
    DISPID_SVSInputWordPosition, DISPID_SVGetVoices, SP_VISEME_3,
    SPRS_INACTIVE, SVESentenceBoundary, ISpeechLexicon,
    DISPID_SVSVisemeId, SPEI_RECO_OTHER_CONTEXT,
    SREPropertyStringChange, DISPID_SPPsCount, DISPID_SRRSaveToMemory,
    SPINTERFERENCE_TOOSLOW, DISPID_SOTGetStorageFileName,
    SDA_No_Trailing_Space, DISPID_SLGenerationId, SP_VISEME_12,
    DISPID_SOTMatchesAttributes, SRAORetainAudio, DISPID_SOTDataKey,
    _ULARGE_INTEGER, DISPID_SPIReplacements, SpeechAddRemoveWord,
    DISPID_SPPNumberOfElements, SAFTCCITT_ALaw_44kHzMono, SP_VISEME_0,
    HRESULT, SPEI_SOUND_END, DISPID_SVSCurrentStreamNumber,
    DISPID_SVEBookmark, DISPID_SVPause, IUnknown,
    DISPID_SRCERequestUI, ISpRecoCategory, ISpeechWaveFormatEx,
    SpeechPropertyComplexResponseSpeed, _lcid, SpeechEngineProperties,
    SP_VISEME_14, SGRSTTDictation, SDTDisplayText, SPCT_SLEEP,
    SPPS_LMA, DISPID_SMSAMMHandle, SPPHRASERULE,
    DISPID_SGRSTs_NewEnum, eLEXTYPE_PRIVATE7, SPFM_OPEN_READWRITE,
    SpeechMicTraining, DISPID_SRGCmdSetRuleState,
    DISPID_SVGetProfiles, DISPID_SPRDisplayAttributes,
    SPEVENTSOURCEINFO, DISPID_SBSSeek, DISPIDSPTSI_SelectionLength,
    SPEI_SR_RETAINEDAUDIO, DISPID_SPCIdToPhone, DISPID_SPRuleParent,
    SRSActiveAlways, SPPS_Modifier, SPPS_SuppressWord,
    SpeechVoiceCategoryTTSRate, DISPID_SPRules_NewEnum,
    DISPID_SLWLangId, SREStreamStart, DISPID_SGRName,
    DISPID_SWFEBitsPerSample, ISpXMLRecoResult,
    DISPID_SVGetAudioInputs, SpeechRecoProfileProperties,
    SPDKL_CurrentUser, SpeechAudioVolume, DISPID_SPPId,
    SSFMCreateForWrite, DISPID_SPRuleNumberOfElements,
    DISPID_SRRTStreamTime, SPRECOGNIZERSTATUS,
    SWPKnownWordPronounceable, DISPID_SRRAudioFormat, SPEI_RESERVED1,
    SpeechGrammarTagDictation, DISPID_SGRSTsItem,
    SDA_Two_Trailing_Spaces, SPEI_PROPERTY_STRING_CHANGE,
    SAFTCCITT_uLaw_22kHzMono, SpObjectTokenCategory,
    DISPID_SLPSymbolic, SPAR_High, DISPID_SRRAlternates,
    SAFT32kHz8BitMono, SpeechPropertyHighConfidenceThreshold,
    ISpeechPhraseReplacements, ISpeechLexiconWord, DISPID_SGRSTRule,
    DISPID_SPPsItem, DISPID_SDKSetStringValue, eLEXTYPE_RESERVED7,
    DISPID_SWFEBlockAlign, SPINTERFERENCE_NOISE, eLEXTYPE_PRIVATE9,
    SPAR_Unknown, DISPID_SRProfile, SPEI_VOICE_CHANGE, SP_VISEME_15,
    SP_VISEME_19, DISPID_SRGSetWordSequenceData, SPAS_RUN,
    DISPIDSPTSI_ActiveOffset, DISPID_SPPConfidence, SRTStandard,
    SAFTGSM610_44kHzMono,
    DISPID_SRAllowAudioInputFormatChangesOnNextSet,
    SAFTADPCM_11kHzStereo, DISPID_SLPLangId, ISpeechAudio
)


class SpeechSpecialTransitionType(IntFlag):
    SSTTWildcard = 1
    SSTTDictation = 2
    SSTTTextBuffer = 3


class SpeechAudioState(IntFlag):
    SASClosed = 0
    SASStop = 1
    SASPause = 2
    SASRun = 3


class SpeechStreamFileMode(IntFlag):
    SSFMOpenForRead = 0
    SSFMOpenReadWrite = 1
    SSFMCreate = 2
    SSFMCreateForWrite = 3


class SpeechStreamSeekPositionType(IntFlag):
    SSSPTRelativeToStart = 0
    SSSPTRelativeToCurrentPosition = 1
    SSSPTRelativeToEnd = 2


class SpeechRunState(IntFlag):
    SRSEDone = 1
    SRSEIsSpeaking = 2


class SpeechTokenContext(IntFlag):
    STCInprocServer = 1
    STCInprocHandler = 2
    STCLocalServer = 4
    STCRemoteServer = 16
    STCAll = 23


class SpeechTokenShellFolder(IntFlag):
    STSF_AppData = 26
    STSF_LocalAppData = 28
    STSF_CommonAppData = 35
    STSF_FlagCreate = 32768


class _SPAUDIOSTATE(IntFlag):
    SPAS_CLOSED = 0
    SPAS_STOP = 1
    SPAS_PAUSE = 2
    SPAS_RUN = 3


class SpeechInterference(IntFlag):
    SINone = 0
    SINoise = 1
    SINoSignal = 2
    SITooLoud = 3
    SITooQuiet = 4
    SITooFast = 5
    SITooSlow = 6


class SPSEMANTICFORMAT(IntFlag):
    SPSMF_SAPI_PROPERTIES = 0
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS = 1
    SPSMF_SRGS_SAPIPROPERTIES = 2
    SPSMF_UPS = 4
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C = 8


class SPGRAMMARWORDTYPE(IntFlag):
    SPWT_DISPLAY = 0
    SPWT_LEXICAL = 1
    SPWT_PRONUNCIATION = 2
    SPWT_LEXICAL_NO_SPECIAL_CHARS = 3


class SpeechDataKeyLocation(IntFlag):
    SDKLDefaultLocation = 0
    SDKLCurrentUser = 1
    SDKLLocalMachine = 2
    SDKLCurrentConfig = 5


class SPFILEMODE(IntFlag):
    SPFM_OPEN_READONLY = 0
    SPFM_OPEN_READWRITE = 1
    SPFM_CREATE = 2
    SPFM_CREATE_ALWAYS = 3
    SPFM_NUM_MODES = 4


class SPLOADOPTIONS(IntFlag):
    SPLO_STATIC = 0
    SPLO_DYNAMIC = 1


class SPVPRIORITY(IntFlag):
    SPVPRI_NORMAL = 0
    SPVPRI_ALERT = 1
    SPVPRI_OVER = 2


class SPEVENTENUM(IntFlag):
    SPEI_UNDEFINED = 0
    SPEI_START_INPUT_STREAM = 1
    SPEI_END_INPUT_STREAM = 2
    SPEI_VOICE_CHANGE = 3
    SPEI_TTS_BOOKMARK = 4
    SPEI_WORD_BOUNDARY = 5
    SPEI_PHONEME = 6
    SPEI_SENTENCE_BOUNDARY = 7
    SPEI_VISEME = 8
    SPEI_TTS_AUDIO_LEVEL = 9
    SPEI_TTS_PRIVATE = 15
    SPEI_MIN_TTS = 1
    SPEI_MAX_TTS = 15
    SPEI_END_SR_STREAM = 34
    SPEI_SOUND_START = 35
    SPEI_SOUND_END = 36
    SPEI_PHRASE_START = 37
    SPEI_RECOGNITION = 38
    SPEI_HYPOTHESIS = 39
    SPEI_SR_BOOKMARK = 40
    SPEI_PROPERTY_NUM_CHANGE = 41
    SPEI_PROPERTY_STRING_CHANGE = 42
    SPEI_FALSE_RECOGNITION = 43
    SPEI_INTERFERENCE = 44
    SPEI_REQUEST_UI = 45
    SPEI_RECO_STATE_CHANGE = 46
    SPEI_ADAPTATION = 47
    SPEI_START_SR_STREAM = 48
    SPEI_RECO_OTHER_CONTEXT = 49
    SPEI_SR_AUDIO_LEVEL = 50
    SPEI_SR_RETAINEDAUDIO = 51
    SPEI_SR_PRIVATE = 52
    SPEI_ACTIVE_CATEGORY_CHANGED = 53
    SPEI_RESERVED5 = 54
    SPEI_RESERVED6 = 55
    SPEI_MIN_SR = 34
    SPEI_MAX_SR = 55
    SPEI_RESERVED1 = 30
    SPEI_RESERVED2 = 33
    SPEI_RESERVED3 = 63


class SpeechLoadOption(IntFlag):
    SLOStatic = 0
    SLODynamic = 1


class SPRULESTATE(IntFlag):
    SPRS_INACTIVE = 0
    SPRS_ACTIVE = 1
    SPRS_ACTIVE_WITH_AUTO_PAUSE = 3
    SPRS_ACTIVE_USER_DELIMITED = 4


class SpeechGrammarState(IntFlag):
    SGSEnabled = 1
    SGSDisabled = 0
    SGSExclusive = 3


class SpeechRuleState(IntFlag):
    SGDSInactive = 0
    SGDSActive = 1
    SGDSActiveWithAutoPause = 3
    SGDSActiveUserDelimited = 4


class SpeechWordPronounceable(IntFlag):
    SWPUnknownWordUnpronounceable = 0
    SWPUnknownWordPronounceable = 1
    SWPKnownWordPronounceable = 2


class SpeechRuleAttributes(IntFlag):
    SRATopLevel = 1
    SRADefaultToActive = 2
    SRAExport = 4
    SRAImport = 8
    SRAInterpreter = 16
    SRADynamic = 32
    SRARoot = 64


class SPWORDPRONOUNCEABLE(IntFlag):
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE = 0
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE = 1
    SPWP_KNOWN_WORD_PRONOUNCEABLE = 2


class SPGRAMMARSTATE(IntFlag):
    SPGS_DISABLED = 0
    SPGS_ENABLED = 1
    SPGS_EXCLUSIVE = 3


class SPINTERFERENCE(IntFlag):
    SPINTERFERENCE_NONE = 0
    SPINTERFERENCE_NOISE = 1
    SPINTERFERENCE_NOSIGNAL = 2
    SPINTERFERENCE_TOOLOUD = 3
    SPINTERFERENCE_TOOQUIET = 4
    SPINTERFERENCE_TOOFAST = 5
    SPINTERFERENCE_TOOSLOW = 6
    SPINTERFERENCE_LATENCY_WARNING = 7
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN = 8
    SPINTERFERENCE_LATENCY_TRUNCATE_END = 9


class SpeechGrammarWordType(IntFlag):
    SGDisplay = 0
    SGLexical = 1
    SGPronounciation = 2
    SGLexicalNoSpecialChars = 3


class SPAUDIOOPTIONS(IntFlag):
    SPAO_NONE = 0
    SPAO_RETAIN_AUDIO = 1


class SPBOOKMARKOPTIONS(IntFlag):
    SPBO_NONE = 0
    SPBO_PAUSE = 1
    SPBO_AHEAD = 2
    SPBO_TIME_UNITS = 4


class SPCONTEXTSTATE(IntFlag):
    SPCS_DISABLED = 0
    SPCS_ENABLED = 1


class SpeechGrammarRuleStateTransitionType(IntFlag):
    SGRSTTEpsilon = 0
    SGRSTTWord = 1
    SGRSTTRule = 2
    SGRSTTDictation = 3
    SGRSTTWildcard = 4
    SGRSTTTextBuffer = 5


class SPRECOSTATE(IntFlag):
    SPRST_INACTIVE = 0
    SPRST_ACTIVE = 1
    SPRST_ACTIVE_ALWAYS = 2
    SPRST_INACTIVE_WITH_PURGE = 3
    SPRST_NUM_STATES = 4


class SPWAVEFORMATTYPE(IntFlag):
    SPWF_INPUT = 0
    SPWF_SRENGINE = 1


class SpeechAudioFormatType(IntEnum):
    SAFTDefault = -1
    SAFTNoAssignedFormat = 0
    SAFTText = 1
    SAFTNonStandardFormat = 2
    SAFTExtendedAudioFormat = 3
    SAFT8kHz8BitMono = 4
    SAFT8kHz8BitStereo = 5
    SAFT8kHz16BitMono = 6
    SAFT8kHz16BitStereo = 7
    SAFT11kHz8BitMono = 8
    SAFT11kHz8BitStereo = 9
    SAFT11kHz16BitMono = 10
    SAFT11kHz16BitStereo = 11
    SAFT12kHz8BitMono = 12
    SAFT12kHz8BitStereo = 13
    SAFT12kHz16BitMono = 14
    SAFT12kHz16BitStereo = 15
    SAFT16kHz8BitMono = 16
    SAFT16kHz8BitStereo = 17
    SAFT16kHz16BitMono = 18
    SAFT16kHz16BitStereo = 19
    SAFT22kHz8BitMono = 20
    SAFT22kHz8BitStereo = 21
    SAFT22kHz16BitMono = 22
    SAFT22kHz16BitStereo = 23
    SAFT24kHz8BitMono = 24
    SAFT24kHz8BitStereo = 25
    SAFT24kHz16BitMono = 26
    SAFT24kHz16BitStereo = 27
    SAFT32kHz8BitMono = 28
    SAFT32kHz8BitStereo = 29
    SAFT32kHz16BitMono = 30
    SAFT32kHz16BitStereo = 31
    SAFT44kHz8BitMono = 32
    SAFT44kHz8BitStereo = 33
    SAFT44kHz16BitMono = 34
    SAFT44kHz16BitStereo = 35
    SAFT48kHz8BitMono = 36
    SAFT48kHz8BitStereo = 37
    SAFT48kHz16BitMono = 38
    SAFT48kHz16BitStereo = 39
    SAFTTrueSpeech_8kHz1BitMono = 40
    SAFTCCITT_ALaw_8kHzMono = 41
    SAFTCCITT_ALaw_8kHzStereo = 42
    SAFTCCITT_ALaw_11kHzMono = 43
    SAFTCCITT_ALaw_11kHzStereo = 44
    SAFTCCITT_ALaw_22kHzMono = 45
    SAFTCCITT_ALaw_22kHzStereo = 46
    SAFTCCITT_ALaw_44kHzMono = 47
    SAFTCCITT_ALaw_44kHzStereo = 48
    SAFTCCITT_uLaw_8kHzMono = 49
    SAFTCCITT_uLaw_8kHzStereo = 50
    SAFTCCITT_uLaw_11kHzMono = 51
    SAFTCCITT_uLaw_11kHzStereo = 52
    SAFTCCITT_uLaw_22kHzMono = 53
    SAFTCCITT_uLaw_22kHzStereo = 54
    SAFTCCITT_uLaw_44kHzMono = 55
    SAFTCCITT_uLaw_44kHzStereo = 56
    SAFTADPCM_8kHzMono = 57
    SAFTADPCM_8kHzStereo = 58
    SAFTADPCM_11kHzMono = 59
    SAFTADPCM_11kHzStereo = 60
    SAFTADPCM_22kHzMono = 61
    SAFTADPCM_22kHzStereo = 62
    SAFTADPCM_44kHzMono = 63
    SAFTADPCM_44kHzStereo = 64
    SAFTGSM610_8kHzMono = 65
    SAFTGSM610_11kHzMono = 66
    SAFTGSM610_22kHzMono = 67
    SAFTGSM610_44kHzMono = 68


class SpeechVoiceSpeakFlags(IntEnum):
    SVSFDefault = 0
    SVSFlagsAsync = 1
    SVSFPurgeBeforeSpeak = 2
    SVSFIsFilename = 4
    SVSFIsXML = 8
    SVSFIsNotXML = 16
    SVSFPersistXML = 32
    SVSFNLPSpeakPunc = 64
    SVSFParseSapi = 128
    SVSFParseSsml = 256
    SVSFParseAutodetect = 0
    SVSFNLPMask = 64
    SVSFParseMask = 384
    SVSFVoiceMask = 511
    SVSFUnusedFlags = -512


class SpeechDiscardType(IntFlag):
    SDTProperty = 1
    SDTReplacement = 2
    SDTRule = 4
    SDTDisplayText = 8
    SDTLexicalForm = 16
    SDTPronunciation = 32
    SDTAudio = 64
    SDTAlternates = 128
    SDTAll = 255


class SpeechDisplayAttributes(IntFlag):
    SDA_No_Trailing_Space = 0
    SDA_One_Trailing_Space = 2
    SDA_Two_Trailing_Spaces = 4
    SDA_Consume_Leading_Spaces = 8


class SpeechEngineConfidence(IntEnum):
    SECLowConfidence = -1
    SECNormalConfidence = 0
    SECHighConfidence = 1


class SPADAPTATIONRELEVANCE(IntFlag):
    SPAR_Unknown = 0
    SPAR_Low = 1
    SPAR_Medium = 2
    SPAR_High = 3


class SPCATEGORYTYPE(IntFlag):
    SPCT_COMMAND = 0
    SPCT_DICTATION = 1
    SPCT_SLEEP = 2
    SPCT_SUB_COMMAND = 3
    SPCT_SUB_DICTATION = 4


class SPLEXICONTYPE(IntEnum):
    eLEXTYPE_USER = 1
    eLEXTYPE_APP = 2
    eLEXTYPE_VENDORLEXICON = 4
    eLEXTYPE_LETTERTOSOUND = 8
    eLEXTYPE_MORPHOLOGY = 16
    eLEXTYPE_RESERVED4 = 32
    eLEXTYPE_USER_SHORTCUT = 64
    eLEXTYPE_RESERVED6 = 128
    eLEXTYPE_RESERVED7 = 256
    eLEXTYPE_RESERVED8 = 512
    eLEXTYPE_RESERVED9 = 1024
    eLEXTYPE_RESERVED10 = 2048
    eLEXTYPE_PRIVATE1 = 4096
    eLEXTYPE_PRIVATE2 = 8192
    eLEXTYPE_PRIVATE3 = 16384
    eLEXTYPE_PRIVATE4 = 32768
    eLEXTYPE_PRIVATE5 = 65536
    eLEXTYPE_PRIVATE6 = 131072
    eLEXTYPE_PRIVATE7 = 262144
    eLEXTYPE_PRIVATE8 = 524288
    eLEXTYPE_PRIVATE9 = 1048576
    eLEXTYPE_PRIVATE10 = 2097152
    eLEXTYPE_PRIVATE11 = 4194304
    eLEXTYPE_PRIVATE12 = 8388608
    eLEXTYPE_PRIVATE13 = 16777216
    eLEXTYPE_PRIVATE14 = 33554432
    eLEXTYPE_PRIVATE15 = 67108864
    eLEXTYPE_PRIVATE16 = 134217728
    eLEXTYPE_PRIVATE17 = 268435456
    eLEXTYPE_PRIVATE18 = 536870912
    eLEXTYPE_PRIVATE19 = 1073741824
    eLEXTYPE_PRIVATE20 = -2147483648


class SpeechBookmarkOptions(IntFlag):
    SBONone = 0
    SBOPause = 1


class SpeechFormatType(IntFlag):
    SFTInput = 0
    SFTSREngine = 1


class SpeechRecognitionType(IntFlag):
    SRTStandard = 0
    SRTAutopause = 1
    SRTEmulated = 2
    SRTSMLTimeout = 4
    SRTExtendableParse = 8
    SRTReSent = 16


class SPPARTOFSPEECH(IntEnum):
    SPPS_NotOverriden = -1
    SPPS_Unknown = 0
    SPPS_Noun = 4096
    SPPS_Verb = 8192
    SPPS_Modifier = 12288
    SPPS_Function = 16384
    SPPS_Interjection = 20480
    SPPS_Noncontent = 24576
    SPPS_LMA = 28672
    SPPS_SuppressWord = 61440


class SpeechLexiconType(IntFlag):
    SLTUser = 1
    SLTApp = 2


class SpeechWordType(IntFlag):
    SWTAdded = 1
    SWTDeleted = 2


class SpeechPartOfSpeech(IntEnum):
    SPSNotOverriden = -1
    SPSUnknown = 0
    SPSNoun = 4096
    SPSVerb = 8192
    SPSModifier = 12288
    SPSFunction = 16384
    SPSInterjection = 20480
    SPSLMA = 28672
    SPSSuppressWord = 61440


class SPWORDTYPE(IntFlag):
    eWORDTYPE_ADDED = 1
    eWORDTYPE_DELETED = 2


class SPSHORTCUTTYPE(IntEnum):
    SPSHT_NotOverriden = -1
    SPSHT_Unknown = 0
    SPSHT_EMAIL = 4096
    SPSHT_OTHER = 8192
    SPPS_RESERVED1 = 12288
    SPPS_RESERVED2 = 16384
    SPPS_RESERVED3 = 20480
    SPPS_RESERVED4 = 61440


class SpeechRecognizerState(IntFlag):
    SRSInactive = 0
    SRSActive = 1
    SRSActiveAlways = 2
    SRSInactiveWithPurge = 3


class SPXMLRESULTOPTIONS(IntFlag):
    SPXRO_SML = 0
    SPXRO_Alternates_SML = 1


class DISPID_SpeechDataKey(IntFlag):
    DISPID_SDKSetBinaryValue = 1
    DISPID_SDKGetBinaryValue = 2
    DISPID_SDKSetStringValue = 3
    DISPID_SDKGetStringValue = 4
    DISPID_SDKSetLongValue = 5
    DISPID_SDKGetlongValue = 6
    DISPID_SDKOpenKey = 7
    DISPID_SDKCreateKey = 8
    DISPID_SDKDeleteKey = 9
    DISPID_SDKDeleteValue = 10
    DISPID_SDKEnumKeys = 11
    DISPID_SDKEnumValues = 12


class DISPID_SpeechObjectToken(IntFlag):
    DISPID_SOTId = 1
    DISPID_SOTDataKey = 2
    DISPID_SOTCategory = 3
    DISPID_SOTGetDescription = 4
    DISPID_SOTSetId = 5
    DISPID_SOTGetAttribute = 6
    DISPID_SOTCreateInstance = 7
    DISPID_SOTRemove = 8
    DISPID_SOTGetStorageFileName = 9
    DISPID_SOTRemoveStorageFileName = 10
    DISPID_SOTIsUISupported = 11
    DISPID_SOTDisplayUI = 12
    DISPID_SOTMatchesAttributes = 13


class DISPID_SpeechObjectTokens(IntEnum):
    DISPID_SOTsCount = 1
    DISPID_SOTsItem = 0
    DISPID_SOTs_NewEnum = -4


class SpeechVoiceEvents(IntFlag):
    SVEStartInputStream = 2
    SVEEndInputStream = 4
    SVEVoiceChange = 8
    SVEBookmark = 16
    SVEWordBoundary = 32
    SVEPhoneme = 64
    SVESentenceBoundary = 128
    SVEViseme = 256
    SVEAudioLevel = 512
    SVEPrivate = 32768
    SVEAllEvents = 33790


class SpeechVoicePriority(IntFlag):
    SVPNormal = 0
    SVPAlert = 1
    SVPOver = 2


class DISPID_SpeechObjectTokenCategory(IntFlag):
    DISPID_SOTCId = 1
    DISPID_SOTCDefault = 2
    DISPID_SOTCSetId = 3
    DISPID_SOTCGetDataKey = 4
    DISPID_SOTCEnumerateTokens = 5


class DISPID_SpeechAudioFormat(IntFlag):
    DISPID_SAFType = 1
    DISPID_SAFGuid = 2
    DISPID_SAFGetWaveFormatEx = 3
    DISPID_SAFSetWaveFormatEx = 4


class DISPID_SpeechBaseStream(IntFlag):
    DISPID_SBSFormat = 1
    DISPID_SBSRead = 2
    DISPID_SBSWrite = 3
    DISPID_SBSSeek = 4


class DISPID_SpeechAudio(IntFlag):
    DISPID_SAStatus = 200
    DISPID_SABufferInfo = 201
    DISPID_SADefaultFormat = 202
    DISPID_SAVolume = 203
    DISPID_SABufferNotifySize = 204
    DISPID_SAEventHandle = 205
    DISPID_SASetState = 206


class DISPID_SpeechMMSysAudio(IntFlag):
    DISPID_SMSADeviceId = 300
    DISPID_SMSALineId = 301
    DISPID_SMSAMMHandle = 302


class SPDATAKEYLOCATION(IntFlag):
    SPDKL_DefaultLocation = 0
    SPDKL_CurrentUser = 1
    SPDKL_LocalMachine = 2
    SPDKL_CurrentConfig = 5


class DISPID_SpeechFileStream(IntFlag):
    DISPID_SFSOpen = 100
    DISPID_SFSClose = 101


class DISPID_SpeechCustomStream(IntFlag):
    DISPID_SCSBaseStream = 100


class SpeechRecoEvents(IntFlag):
    SREStreamEnd = 1
    SRESoundStart = 2
    SRESoundEnd = 4
    SREPhraseStart = 8
    SRERecognition = 16
    SREHypothesis = 32
    SREBookmark = 64
    SREPropertyNumChange = 128
    SREPropertyStringChange = 256
    SREFalseRecognition = 512
    SREInterference = 1024
    SRERequestUI = 2048
    SREStateChange = 4096
    SREAdaptation = 8192
    SREStreamStart = 16384
    SRERecoOtherContext = 32768
    SREAudioLevel = 65536
    SREPrivate = 262144
    SREAllEvents = 393215


class DISPID_SpeechMemoryStream(IntFlag):
    DISPID_SMSSetData = 100
    DISPID_SMSGetData = 101


class DISPID_SpeechAudioStatus(IntFlag):
    DISPID_SASFreeBufferSpace = 1
    DISPID_SASNonBlockingIO = 2
    DISPID_SASState = 3
    DISPID_SASCurrentSeekPosition = 4
    DISPID_SASCurrentDevicePosition = 5


class DISPID_SpeechAudioBufferInfo(IntFlag):
    DISPID_SABIMinNotification = 1
    DISPID_SABIBufferSize = 2
    DISPID_SABIEventBias = 3


class DISPID_SpeechWaveFormatEx(IntFlag):
    DISPID_SWFEFormatTag = 1
    DISPID_SWFEChannels = 2
    DISPID_SWFESamplesPerSec = 3
    DISPID_SWFEAvgBytesPerSec = 4
    DISPID_SWFEBlockAlign = 5
    DISPID_SWFEBitsPerSample = 6
    DISPID_SWFEExtraData = 7


class SpeechRecoContextState(IntFlag):
    SRCS_Disabled = 0
    SRCS_Enabled = 1


class DISPID_SpeechVoice(IntFlag):
    DISPID_SVStatus = 1
    DISPID_SVVoice = 2
    DISPID_SVAudioOutput = 3
    DISPID_SVAudioOutputStream = 4
    DISPID_SVRate = 5
    DISPID_SVVolume = 6
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet = 7
    DISPID_SVEventInterests = 8
    DISPID_SVPriority = 9
    DISPID_SVAlertBoundary = 10
    DISPID_SVSyncronousSpeakTimeout = 11
    DISPID_SVSpeak = 12
    DISPID_SVSpeakStream = 13
    DISPID_SVPause = 14
    DISPID_SVResume = 15
    DISPID_SVSkip = 16
    DISPID_SVGetVoices = 17
    DISPID_SVGetAudioOutputs = 18
    DISPID_SVWaitUntilDone = 19
    DISPID_SVSpeakCompleteEvent = 20
    DISPID_SVIsUISupported = 21
    DISPID_SVDisplayUI = 22


class DISPID_SpeechVoiceStatus(IntFlag):
    DISPID_SVSCurrentStreamNumber = 1
    DISPID_SVSLastStreamNumberQueued = 2
    DISPID_SVSLastResult = 3
    DISPID_SVSRunningState = 4
    DISPID_SVSInputWordPosition = 5
    DISPID_SVSInputWordLength = 6
    DISPID_SVSInputSentencePosition = 7
    DISPID_SVSInputSentenceLength = 8
    DISPID_SVSLastBookmark = 9
    DISPID_SVSLastBookmarkId = 10
    DISPID_SVSPhonemeId = 11
    DISPID_SVSVisemeId = 12


class DISPID_SpeechVoiceEvent(IntFlag):
    DISPID_SVEStreamStart = 1
    DISPID_SVEStreamEnd = 2
    DISPID_SVEVoiceChange = 3
    DISPID_SVEBookmark = 4
    DISPID_SVEWord = 5
    DISPID_SVEPhoneme = 6
    DISPID_SVESentenceBoundary = 7
    DISPID_SVEViseme = 8
    DISPID_SVEAudioLevel = 9
    DISPID_SVEEnginePrivate = 10


class DISPID_SpeechRecognizer(IntFlag):
    DISPID_SRRecognizer = 1
    DISPID_SRAllowAudioInputFormatChangesOnNextSet = 2
    DISPID_SRAudioInput = 3
    DISPID_SRAudioInputStream = 4
    DISPID_SRIsShared = 5
    DISPID_SRState = 6
    DISPID_SRStatus = 7
    DISPID_SRProfile = 8
    DISPID_SREmulateRecognition = 9
    DISPID_SRCreateRecoContext = 10
    DISPID_SRGetFormat = 11
    DISPID_SRSetPropertyNumber = 12
    DISPID_SRGetPropertyNumber = 13
    DISPID_SRSetPropertyString = 14
    DISPID_SRGetPropertyString = 15
    DISPID_SRIsUISupported = 16
    DISPID_SRDisplayUI = 17
    DISPID_SRGetRecognizers = 18
    DISPID_SVGetAudioInputs = 19
    DISPID_SVGetProfiles = 20


class SpeechEmulationCompareFlags(IntFlag):
    SECFIgnoreCase = 1
    SECFIgnoreKanaType = 65536
    SECFIgnoreWidth = 131072
    SECFNoSpecialChars = 536870912
    SECFEmulateResult = 1073741824
    SECFDefault = 196609


class DISPID_SpeechRecognizerStatus(IntFlag):
    DISPID_SRSAudioStatus = 1
    DISPID_SRSCurrentStreamPosition = 2
    DISPID_SRSCurrentStreamNumber = 3
    DISPID_SRSNumberOfActiveRules = 4
    DISPID_SRSClsidEngine = 5
    DISPID_SRSSupportedLanguages = 6


class DISPID_SpeechRecoContext(IntFlag):
    DISPID_SRCRecognizer = 1
    DISPID_SRCAudioInInterferenceStatus = 2
    DISPID_SRCRequestedUIType = 3
    DISPID_SRCVoice = 4
    DISPID_SRAllowVoiceFormatMatchingOnNextSet = 5
    DISPID_SRCVoicePurgeEvent = 6
    DISPID_SRCEventInterests = 7
    DISPID_SRCCmdMaxAlternates = 8
    DISPID_SRCState = 9
    DISPID_SRCRetainedAudio = 10
    DISPID_SRCRetainedAudioFormat = 11
    DISPID_SRCPause = 12
    DISPID_SRCResume = 13
    DISPID_SRCCreateGrammar = 14
    DISPID_SRCCreateResultFromMemory = 15
    DISPID_SRCBookmark = 16
    DISPID_SRCSetAdaptationData = 17


class DISPIDSPRG(IntFlag):
    DISPID_SRGId = 1
    DISPID_SRGRecoContext = 2
    DISPID_SRGState = 3
    DISPID_SRGRules = 4
    DISPID_SRGReset = 5
    DISPID_SRGCommit = 6
    DISPID_SRGCmdLoadFromFile = 7
    DISPID_SRGCmdLoadFromObject = 8
    DISPID_SRGCmdLoadFromResource = 9
    DISPID_SRGCmdLoadFromMemory = 10
    DISPID_SRGCmdLoadFromProprietaryGrammar = 11
    DISPID_SRGCmdSetRuleState = 12
    DISPID_SRGCmdSetRuleIdState = 13
    DISPID_SRGDictationLoad = 14
    DISPID_SRGDictationUnload = 15
    DISPID_SRGDictationSetState = 16
    DISPID_SRGSetWordSequenceData = 17
    DISPID_SRGSetTextSelection = 18
    DISPID_SRGIsPronounceable = 19


class DISPID_SpeechRecoContextEvents(IntFlag):
    DISPID_SRCEStartStream = 1
    DISPID_SRCEEndStream = 2
    DISPID_SRCEBookmark = 3
    DISPID_SRCESoundStart = 4
    DISPID_SRCESoundEnd = 5
    DISPID_SRCEPhraseStart = 6
    DISPID_SRCERecognition = 7
    DISPID_SRCEHypothesis = 8
    DISPID_SRCEPropertyNumberChange = 9
    DISPID_SRCEPropertyStringChange = 10
    DISPID_SRCEFalseRecognition = 11
    DISPID_SRCEInterference = 12
    DISPID_SRCERequestUI = 13
    DISPID_SRCERecognizerStateChange = 14
    DISPID_SRCEAdaptation = 15
    DISPID_SRCERecognitionForOtherContext = 16
    DISPID_SRCEAudioLevel = 17
    DISPID_SRCEEnginePrivate = 18


class DISPID_SpeechGrammarRule(IntFlag):
    DISPID_SGRAttributes = 1
    DISPID_SGRInitialState = 2
    DISPID_SGRName = 3
    DISPID_SGRId = 4
    DISPID_SGRClear = 5
    DISPID_SGRAddResource = 6
    DISPID_SGRAddState = 7


class DISPID_SpeechGrammarRules(IntEnum):
    DISPID_SGRsCount = 1
    DISPID_SGRsDynamic = 2
    DISPID_SGRsAdd = 3
    DISPID_SGRsCommit = 4
    DISPID_SGRsCommitAndSave = 5
    DISPID_SGRsFindRule = 6
    DISPID_SGRsItem = 0
    DISPID_SGRs_NewEnum = -4


class DISPID_SpeechGrammarRuleState(IntFlag):
    DISPID_SGRSRule = 1
    DISPID_SGRSTransitions = 2
    DISPID_SGRSAddWordTransition = 3
    DISPID_SGRSAddRuleTransition = 4
    DISPID_SGRSAddSpecialTransition = 5


class DISPID_SpeechGrammarRuleStateTransitions(IntEnum):
    DISPID_SGRSTsCount = 1
    DISPID_SGRSTsItem = 0
    DISPID_SGRSTs_NewEnum = -4


class DISPID_SpeechGrammarRuleStateTransition(IntFlag):
    DISPID_SGRSTType = 1
    DISPID_SGRSTText = 2
    DISPID_SGRSTRule = 3
    DISPID_SGRSTWeight = 4
    DISPID_SGRSTPropertyName = 5
    DISPID_SGRSTPropertyId = 6
    DISPID_SGRSTPropertyValue = 7
    DISPID_SGRSTNextState = 8


class DISPIDSPTSI(IntFlag):
    DISPIDSPTSI_ActiveOffset = 1
    DISPIDSPTSI_ActiveLength = 2
    DISPIDSPTSI_SelectionOffset = 3
    DISPIDSPTSI_SelectionLength = 4


class DISPID_SpeechRecoResult(IntFlag):
    DISPID_SRRRecoContext = 1
    DISPID_SRRTimes = 2
    DISPID_SRRAudioFormat = 3
    DISPID_SRRPhraseInfo = 4
    DISPID_SRRAlternates = 5
    DISPID_SRRAudio = 6
    DISPID_SRRSpeakAudio = 7
    DISPID_SRRSaveToMemory = 8
    DISPID_SRRDiscardResultInfo = 9


class DISPID_SpeechXMLRecoResult(IntFlag):
    DISPID_SRRGetXMLResult = 10
    DISPID_SRRGetXMLErrorInfo = 11


class DISPID_SpeechRecoResult2(IntFlag):
    DISPID_SRRSetTextFeedback = 12


class DISPID_SpeechPhraseBuilder(IntFlag):
    DISPID_SPPBRestorePhraseFromMemory = 1


class DISPID_SpeechRecoResultTimes(IntFlag):
    DISPID_SRRTStreamTime = 1
    DISPID_SRRTLength = 2
    DISPID_SRRTTickCount = 3
    DISPID_SRRTOffsetFromStart = 4


class DISPID_SpeechPhraseAlternate(IntFlag):
    DISPID_SPARecoResult = 1
    DISPID_SPAStartElementInResult = 2
    DISPID_SPANumberOfElementsInResult = 3
    DISPID_SPAPhraseInfo = 4
    DISPID_SPACommit = 5


class DISPID_SpeechPhraseAlternates(IntEnum):
    DISPID_SPAsCount = 1
    DISPID_SPAsItem = 0
    DISPID_SPAs_NewEnum = -4


class DISPID_SpeechPhraseInfo(IntFlag):
    DISPID_SPILanguageId = 1
    DISPID_SPIGrammarId = 2
    DISPID_SPIStartTime = 3
    DISPID_SPIAudioStreamPosition = 4
    DISPID_SPIAudioSizeBytes = 5
    DISPID_SPIRetainedSizeBytes = 6
    DISPID_SPIAudioSizeTime = 7
    DISPID_SPIRule = 8
    DISPID_SPIProperties = 9
    DISPID_SPIElements = 10
    DISPID_SPIReplacements = 11
    DISPID_SPIEngineId = 12
    DISPID_SPIEnginePrivateData = 13
    DISPID_SPISaveToMemory = 14
    DISPID_SPIGetText = 15
    DISPID_SPIGetDisplayAttributes = 16


class DISPID_SpeechPhraseElement(IntFlag):
    DISPID_SPEAudioTimeOffset = 1
    DISPID_SPEAudioSizeTime = 2
    DISPID_SPEAudioStreamOffset = 3
    DISPID_SPEAudioSizeBytes = 4
    DISPID_SPERetainedStreamOffset = 5
    DISPID_SPERetainedSizeBytes = 6
    DISPID_SPEDisplayText = 7
    DISPID_SPELexicalForm = 8
    DISPID_SPEPronunciation = 9
    DISPID_SPEDisplayAttributes = 10
    DISPID_SPERequiredConfidence = 11
    DISPID_SPEActualConfidence = 12
    DISPID_SPEEngineConfidence = 13


class DISPID_SpeechPhraseElements(IntEnum):
    DISPID_SPEsCount = 1
    DISPID_SPEsItem = 0
    DISPID_SPEs_NewEnum = -4


class DISPID_SpeechPhraseReplacement(IntFlag):
    DISPID_SPRDisplayAttributes = 1
    DISPID_SPRText = 2
    DISPID_SPRFirstElement = 3
    DISPID_SPRNumberOfElements = 4


class DISPID_SpeechPhraseReplacements(IntEnum):
    DISPID_SPRsCount = 1
    DISPID_SPRsItem = 0
    DISPID_SPRs_NewEnum = -4


class DISPID_SpeechPhraseProperty(IntFlag):
    DISPID_SPPName = 1
    DISPID_SPPId = 2
    DISPID_SPPValue = 3
    DISPID_SPPFirstElement = 4
    DISPID_SPPNumberOfElements = 5
    DISPID_SPPEngineConfidence = 6
    DISPID_SPPConfidence = 7
    DISPID_SPPParent = 8
    DISPID_SPPChildren = 9


class DISPID_SpeechPhraseProperties(IntEnum):
    DISPID_SPPsCount = 1
    DISPID_SPPsItem = 0
    DISPID_SPPs_NewEnum = -4


class DISPID_SpeechPhraseRule(IntFlag):
    DISPID_SPRuleName = 1
    DISPID_SPRuleId = 2
    DISPID_SPRuleFirstElement = 3
    DISPID_SPRuleNumberOfElements = 4
    DISPID_SPRuleParent = 5
    DISPID_SPRuleChildren = 6
    DISPID_SPRuleConfidence = 7
    DISPID_SPRuleEngineConfidence = 8


class DISPID_SpeechPhraseRules(IntEnum):
    DISPID_SPRulesCount = 1
    DISPID_SPRulesItem = 0
    DISPID_SPRules_NewEnum = -4


class SpeechRetainedAudioOptions(IntFlag):
    SRAONone = 0
    SRAORetainAudio = 1


class DISPID_SpeechLexicon(IntFlag):
    DISPID_SLGenerationId = 1
    DISPID_SLGetWords = 2
    DISPID_SLAddPronunciation = 3
    DISPID_SLAddPronunciationByPhoneIds = 4
    DISPID_SLRemovePronunciation = 5
    DISPID_SLRemovePronunciationByPhoneIds = 6
    DISPID_SLGetPronunciations = 7
    DISPID_SLGetGenerationChange = 8


class DISPID_SpeechLexiconWords(IntEnum):
    DISPID_SLWsCount = 1
    DISPID_SLWsItem = 0
    DISPID_SLWs_NewEnum = -4


class DISPID_SpeechLexiconWord(IntFlag):
    DISPID_SLWLangId = 1
    DISPID_SLWType = 2
    DISPID_SLWWord = 3
    DISPID_SLWPronunciations = 4


class DISPID_SpeechLexiconProns(IntEnum):
    DISPID_SLPsCount = 1
    DISPID_SLPsItem = 0
    DISPID_SLPs_NewEnum = -4


class DISPID_SpeechLexiconPronunciation(IntFlag):
    DISPID_SLPType = 1
    DISPID_SLPLangId = 2
    DISPID_SLPPartOfSpeech = 3
    DISPID_SLPPhoneIds = 4
    DISPID_SLPSymbolic = 5


class DISPID_SpeechPhoneConverter(IntFlag):
    DISPID_SPCLangId = 1
    DISPID_SPCPhoneToId = 2
    DISPID_SPCIdToPhone = 3


class SpeechVisemeFeature(IntFlag):
    SVF_None = 0
    SVF_Stressed = 1
    SVF_Emphasis = 2


class SpeechVisemeType(IntFlag):
    SVP_0 = 0
    SVP_1 = 1
    SVP_2 = 2
    SVP_3 = 3
    SVP_4 = 4
    SVP_5 = 5
    SVP_6 = 6
    SVP_7 = 7
    SVP_8 = 8
    SVP_9 = 9
    SVP_10 = 10
    SVP_11 = 11
    SVP_12 = 12
    SVP_13 = 13
    SVP_14 = 14
    SVP_15 = 15
    SVP_16 = 16
    SVP_17 = 17
    SVP_18 = 18
    SVP_19 = 19
    SVP_20 = 20
    SVP_21 = 21


class SPVISEMES(IntFlag):
    SP_VISEME_0 = 0
    SP_VISEME_1 = 1
    SP_VISEME_2 = 2
    SP_VISEME_3 = 3
    SP_VISEME_4 = 4
    SP_VISEME_5 = 5
    SP_VISEME_6 = 6
    SP_VISEME_7 = 7
    SP_VISEME_8 = 8
    SP_VISEME_9 = 9
    SP_VISEME_10 = 10
    SP_VISEME_11 = 11
    SP_VISEME_12 = 12
    SP_VISEME_13 = 13
    SP_VISEME_14 = 14
    SP_VISEME_15 = 15
    SP_VISEME_16 = 16
    SP_VISEME_17 = 17
    SP_VISEME_18 = 18
    SP_VISEME_19 = 19
    SP_VISEME_20 = 20
    SP_VISEME_21 = 21


SPAUDIOSTATE = _SPAUDIOSTATE
SPSTREAMFORMATTYPE = SPWAVEFORMATTYPE


__all__ = [
    '__MIDL_IWinTypes_0009', 'SECFEmulateResult',
    'SAFTGSM610_11kHzMono', 'DISPID_SBSRead', 'SPPHRASE',
    'eLEXTYPE_PRIVATE13', 'DISPID_SRRTimes', 'DISPID_SPPFirstElement',
    'SREStateChange', 'ISpeechPhraseProperties', 'SVSFParseSsml',
    'SPFM_CREATE', 'DISPID_SpeechRecoResult', 'DISPID_SGRAttributes',
    'DISPID_SpeechLexiconWords',
    '__MIDL___MIDL_itf_sapi_0000_0020_0001', 'SGRSTTTextBuffer',
    'DISPID_SVSpeakStream', 'eLEXTYPE_PRIVATE5',
    'DISPID_SCSBaseStream', 'ISpeechLexiconPronunciation',
    'SpInprocRecognizer', 'SGSEnabled', 'SP_VISEME_1',
    'DISPID_SOTs_NewEnum', 'SPRULESTATE', 'SAFTADPCM_22kHzMono',
    'DISPID_SGRSTPropertyId', 'SAFT44kHz8BitStereo',
    'eLEXTYPE_RESERVED8', 'ISpRecoResult', 'SVEVoiceChange',
    'DISPID_SBSWrite', 'DISPID_SOTRemove', 'DISPID_SGRSRule',
    'DISPID_SPEs_NewEnum', 'SDTAll', 'SPEI_END_SR_STREAM',
    'SpeechCategoryAppLexicons', 'SRSInactive', 'DISPID_SOTCSetId',
    'SVP_8', 'SRTSMLTimeout', 'SpeechVoiceSpeakFlags',
    'ISpeechRecoResult', 'SRESoundStart', 'DISPID_SVEEnginePrivate',
    'DISPID_SLPPartOfSpeech', 'ISpeechPhraseRules',
    'SPINTERFERENCE_NONE', 'SpeechEmulationCompareFlags',
    'DISPID_SRCCreateGrammar', 'SPEI_INTERFERENCE',
    'DISPID_SGRInitialState', 'SPVOICESTATUS', 'SPXRO_SML',
    'eLEXTYPE_PRIVATE19', 'SFTSREngine', 'SpeechLexiconType',
    'DISPID_SVSpeakCompleteEvent', 'DISPID_SVEventInterests',
    'DISPID_SpeechAudioBufferInfo', 'STCInprocServer',
    'SPSTREAMFORMATTYPE', 'SPCT_SUB_COMMAND', 'SRTReSent',
    'SPRECOSTATE', 'eLEXTYPE_RESERVED6', 'DISPID_SMSADeviceId',
    'SAFTCCITT_uLaw_11kHzStereo', 'DISPID_SPRFirstElement',
    'DISPID_SPRuleChildren', 'DISPID_SPCLangId',
    'DISPID_SVSInputWordLength', 'SPSMF_SRGS_SAPIPROPERTIES',
    'DISPID_SpeechPhraseAlternates', 'SVP_7',
    'ISpeechPhraseAlternates', 'DISPID_SpeechPhraseElement',
    'DISPID_SOTCGetDataKey', 'DISPID_SPIEnginePrivateData',
    'SPEI_START_SR_STREAM', 'ISpStreamFormat', 'SGSDisabled',
    'SPINTERFERENCE_TOOLOUD', 'SPINTERFERENCE_LATENCY_WARNING',
    'ISpRecoContext', 'SSFMOpenForRead', 'SpeechPropertyAdaptationOn',
    'ISpeechPhraseElements', 'DISPID_SRRGetXMLErrorInfo',
    'SITooQuiet', 'SpeechCategoryAudioIn', 'SAFT24kHz16BitStereo',
    'DISPID_SRCERecognitionForOtherContext', 'SP_VISEME_6',
    'Speech_StreamPos_Asap', 'ISpeechFileStream',
    'SpeechPropertyLowConfidenceThreshold',
    'DISPID_SABufferNotifySize', 'SAFT12kHz8BitStereo',
    'DISPID_SMSALineId', 'DISPID_SpeechVoiceStatus',
    'DISPID_SpeechPhraseAlternate', 'SpeechSpecialTransitionType',
    'SVP_3', 'SpSharedRecoContext', 'SAFTGSM610_8kHzMono',
    'SVSFUnusedFlags', 'SPWORD', 'ISpeechLexiconPronunciations',
    'ISpPhoneConverter', 'SVP_20', 'SVP_10', 'ISpeechGrammarRules',
    'SREPropertyNumChange', 'DISPID_SPPName',
    'DISPID_SVSInputSentencePosition', 'ISpEventSource',
    'DISPID_SVSpeak', 'DISPID_SPAPhraseInfo', 'SPRS_ACTIVE',
    'SP_VISEME_16', 'DISPID_SASNonBlockingIO',
    'SpeechCategoryAudioOut', 'ISpSerializeState',
    'SpeechTokenIdUserLexicon',
    'DISPID_SRAllowVoiceFormatMatchingOnNextSet',
    'ISpeechAudioBufferInfo', 'STSF_FlagCreate',
    'SPWP_UNKNOWN_WORD_PRONOUNCEABLE', 'DISPIDSPTSI',
    'DISPID_SGRSTText', 'SGRSTTRule', 'SVSFParseSapi',
    'SpeechTokenKeyAttributes', 'SRAInterpreter', 'SPEI_SR_BOOKMARK',
    'SAFTADPCM_44kHzStereo', 'SLTApp', 'DISPID_SPEEngineConfidence',
    'DISPID_SpeechPhraseProperties', 'SPEI_RESERVED5',
    'SDKLCurrentUser', 'SAFT44kHz8BitMono', 'SDTPronunciation',
    'eLEXTYPE_PRIVATE1', 'SPEI_ADAPTATION', 'eLEXTYPE_PRIVATE4',
    'SECLowConfidence', 'SPSModifier', 'SVPOver', 'DISPID_SBSFormat',
    'DISPID_SRGDictationUnload', 'SPEI_REQUEST_UI',
    'DISPID_SLPPhoneIds', 'SAFT22kHz16BitStereo',
    'DISPID_SGRAddResource', 'DISPID_SAFType', 'SPEI_SR_PRIVATE',
    'DISPID_SRCSetAdaptationData', 'SPPHRASEELEMENT',
    'SAFT48kHz8BitStereo', 'ISpPhoneticAlphabetSelection',
    'SpeechPropertyNormalConfidenceThreshold',
    'DISPID_SRGetPropertyNumber', 'SITooLoud', 'eLEXTYPE_PRIVATE14',
    'SPEI_UNDEFINED', 'DISPID_SPRsCount', 'STCInprocHandler',
    'ISpObjectWithToken', 'DISPID_SLPsItem',
    'SpPhoneticAlphabetConverter', 'LONG_PTR',
    'SPEI_START_INPUT_STREAM', 'SAFT11kHz8BitMono',
    'SWPUnknownWordPronounceable', 'SREAudioLevel', 'DISPID_SASState',
    'SpeechAudioFormatGUIDWave', 'SVP_2', 'SAFT24kHz8BitMono',
    'SRTAutopause', 'SPAS_STOP', 'DISPID_SVAudioOutputStream',
    'DISPID_SpeechFileStream', 'SVP_9',
    'DISPID_SLRemovePronunciation', 'SPEI_HYPOTHESIS',
    'SAFT48kHz8BitMono', 'ISpeechAudioStatus', 'SpeechUserTraining',
    'DISPID_SRGCommit', 'SpeechGrammarRuleStateTransitionType',
    'SVSFPurgeBeforeSpeak', 'DISPID_SABIEventBias', 'SGRSTTWord',
    'STCLocalServer', 'SPDKL_LocalMachine',
    'SDA_Consume_Leading_Spaces', 'SREAdaptation',
    'DISPID_SDKGetlongValue', 'DISPID_SRGState',
    'SpeechTokenShellFolder', 'eLEXTYPE_PRIVATE3',
    'DISPID_SPEActualConfidence', 'DISPID_SGRsCommit', 'SRATopLevel',
    'DISPID_SpeechLexiconWord', 'SECFNoSpecialChars',
    'SpeechWordType', 'SPPS_Verb', 'ISpObjectTokenCategory',
    'SpeechAudioFormatType', 'SREPhraseStart', 'DISPID_SVResume',
    'DISPID_SRGCmdSetRuleIdState', 'DISPID_SGRsCount',
    'ISpeechRecognizerStatus', 'SVEPhoneme',
    'DISPID_SPEAudioStreamOffset', 'DISPID_SpeechGrammarRule',
    'DISPID_SPPParent', 'DISPID_SADefaultFormat',
    'SPXMLRESULTOPTIONS', 'SpeechStreamFileMode', 'SVSFlagsAsync',
    'DISPID_SDKGetBinaryValue', 'DISPID_SOTGetAttribute',
    'DISPID_SPRuleFirstElement', 'DISPID_SRGetRecognizers',
    'DISPID_SRCEAudioLevel', 'SAFTCCITT_uLaw_44kHzStereo',
    'SPINTERFERENCE', 'SAFTADPCM_11kHzMono', 'DISPID_SAEventHandle',
    'DISPID_SRGCmdLoadFromObject', 'SVP_6', 'SSSPTRelativeToStart',
    'SpeechStreamSeekPositionType', 'tagSTATSTG',
    'SPRS_ACTIVE_WITH_AUTO_PAUSE', 'DISPID_SWFEFormatTag',
    'eLEXTYPE_PRIVATE2', 'SPCONTEXTSTATE', 'DISPID_SVEPhoneme',
    'SWPUnknownWordUnpronounceable', 'SpStream', 'SAFT8kHz8BitMono',
    'DISPID_SRCEPropertyStringChange', 'SP_VISEME_20',
    'SPEI_TTS_PRIVATE', 'DISPID_SPPValue', 'DISPID_SGRId',
    'DISPID_SABIMinNotification', 'SVSFParseAutodetect',
    'DISPID_SpeechDataKey', 'DISPID_SpeechRecoContextEvents',
    'SPINTERFERENCE_LATENCY_TRUNCATE_END', 'DISPID_SRSAudioStatus',
    'DISPID_SRIsUISupported', 'DISPID_SRRAudio',
    'DISPID_SPEAudioSizeBytes', 'DISPID_SPEDisplayAttributes',
    'typelib_path', 'DISPID_SOTSetId', 'DISPID_SVVoice',
    'DISPID_SRCERecognizerStateChange',
    'SSSPTRelativeToCurrentPosition', 'SGDisplay',
    'DISPID_SGRs_NewEnum', 'SPBO_AHEAD', 'DISPID_SRCEStartStream',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_W3C', 'DISPID_SPAs_NewEnum',
    'SpeechAudioFormatGUIDText', 'SPCT_SUB_DICTATION',
    'SPEI_END_INPUT_STREAM', 'SAFT11kHz8BitStereo', 'SPEI_MAX_SR',
    'SAFT22kHz8BitMono', 'DISPID_SRCVoicePurgeEvent',
    'DISPID_SDKCreateKey', 'ISpPhoneticAlphabetConverter',
    'DISPID_SLGetGenerationChange', 'SPVPRI_OVER', 'SPVPRIORITY',
    'SPSHORTCUTTYPE', 'SPSVerb', 'ISpStreamFormatConverter',
    'SPXRO_Alternates_SML', 'SPGS_ENABLED', 'DISPID_SGRSTransitions',
    'SAFTADPCM_44kHzMono', 'ISpPhrase', 'DISPID_SGRsAdd',
    'DISPID_SPARecoResult', 'IInternetSecurityMgrSite',
    'ISpObjectToken', 'SAFT11kHz16BitMono',
    'DISPID_SRCCmdMaxAlternates',
    'DISPID_SpeechGrammarRuleStateTransition', 'SPEI_TTS_BOOKMARK',
    'DISPID_SAVolume', 'SAFT48kHz16BitStereo', 'eLEXTYPE_RESERVED9',
    'SAFTText', 'SECFIgnoreCase', 'SpeechGrammarWordType',
    'SREPrivate', 'SpeechDiscardType', 'SDKLCurrentConfig',
    'SPEVENTENUM', 'DISPID_SPEsItem', 'SSFMCreate',
    'SVEEndInputStream', 'DISPID_SOTsItem',
    'SAFTCCITT_uLaw_8kHzStereo', 'DISPID_SDKSetBinaryValue',
    'SPAS_CLOSED', 'SPDKL_CurrentConfig', 'DISPID_SVSPhonemeId',
    'DISPID_SpeechVoiceEvent', 'ISpResourceManager',
    'SAFTCCITT_uLaw_8kHzMono', 'eLEXTYPE_VENDORLEXICON',
    'DISPID_SPRuleEngineConfidence', 'DISPID_SPRulesCount',
    'SASPause', 'DISPID_SRGReset', 'SVF_None', 'SpMemoryStream',
    'DISPID_SpeechLexiconProns', 'SPEI_SENTENCE_BOUNDARY',
    'SpPhraseInfoBuilder', 'SpeechVoiceSkipTypeSentence',
    'ISpProperties', 'SPDATAKEYLOCATION', 'SREInterference',
    'eLEXTYPE_LETTERTOSOUND', 'SPLEXICONTYPE', 'DISPID_SRState',
    'SPADAPTATIONRELEVANCE', 'DISPID_SDKSetLongValue',
    'DISPID_SMSSetData', 'SPFM_NUM_MODES', 'SPSMF_SAPI_PROPERTIES',
    'SDKLLocalMachine', 'DISPID_SRGRecoContext', 'SPFILEMODE',
    'DISPID_SRCRetainedAudioFormat', 'DISPID_SRCRetainedAudio',
    'SDKLDefaultLocation', 'DISPID_SpeechGrammarRules',
    'DISPID_SPIElements', 'DISPID_SpeechLexicon', 'SPEI_PHONEME',
    'SPCS_ENABLED', 'DISPID_SRGDictationSetState',
    'DISPID_SRCEPropertyNumberChange', 'DISPID_SRCEHypothesis',
    'DISPID_SPIEngineId', 'SAFTCCITT_ALaw_22kHzStereo',
    'DISPID_SpeechMemoryStream', 'SVP_1', 'DISPID_SVEVoiceChange',
    'SPAUDIOBUFFERINFO', 'SAFT12kHz16BitStereo', 'DISPID_SLWWord',
    'IEnumString', 'SPSEMANTICERRORINFO', 'SRARoot',
    'SPEI_ACTIVE_CATEGORY_CHANGED', 'SAFT32kHz16BitStereo',
    'SP_VISEME_11', 'SPEI_RECO_STATE_CHANGE', 'SPLO_STATIC',
    'DISPID_SFSOpen', 'DISPID_SVSkip', 'DISPID_SVSLastBookmarkId',
    'SREStreamEnd', 'SPAS_PAUSE', 'ISpeechObjectTokens',
    'SPCT_DICTATION', 'SRERecoOtherContext',
    'DISPID_SRGCmdLoadFromMemory', 'ISpeechPhoneConverter', 'SPSNoun',
    'DISPID_SLGetPronunciations', 'SASClosed', 'SSTTWildcard',
    'SPWP_KNOWN_WORD_PRONOUNCEABLE', 'SVEWordBoundary', 'Library',
    'SPWORDPRONUNCIATION', 'SPPHRASEREPLACEMENT', 'SVSFIsNotXML',
    'DISPID_SAStatus', 'SREAllEvents', 'DISPID_SpeechRecoContext',
    'DISPID_SASetState', 'SAFTDefault', 'DISPID_SVEAudioLevel',
    'DISPID_SABIBufferSize', 'DISPID_SRCESoundStart',
    'DISPID_SRCEInterference', 'SpeechRunState',
    'SpeechRuleAttributes', 'UINT_PTR', 'ISpeechRecoResultTimes',
    'ISpeechRecoResult2', 'eLEXTYPE_PRIVATE10',
    'DISPID_SRSClsidEngine', 'SVEBookmark', 'SPINTERFERENCE_NOSIGNAL',
    'DISPID_SpeechVoice', 'SVP_19', 'SGRSTTEpsilon',
    'SpeechLoadOption', 'ISpRecognizer3', 'DISPID_SVRate',
    'SpShortcut', 'DISPID_SRCESoundEnd', 'SpeechRetainedAudioOptions',
    'DISPID_SLWsItem', 'DISPID_SRCEEnginePrivate', 'SRADynamic',
    'SVP_5', 'DISPID_SPCPhoneToId', 'DISPID_SDKGetStringValue',
    'SAFT44kHz16BitStereo', 'SPWAVEFORMATTYPE', 'DISPID_SVVolume',
    'SPWORDPRONOUNCEABLE', 'DISPID_SLWType', 'SRAImport',
    'DISPID_SPAsCount', 'eLEXTYPE_PRIVATE8', 'SAFT22kHz16BitMono',
    'DISPID_SVESentenceBoundary', 'DISPID_SRCEFalseRecognition',
    'DISPID_SVSRunningState', 'SAFTExtendedAudioFormat',
    'SAFT24kHz8BitStereo', 'ISpNotifySink', 'SVSFPersistXML',
    'tagSPPROPERTYINFO', 'SPINTERFERENCE_TOOFAST', 'SPEI_SOUND_START',
    'ISpeechGrammarRuleStateTransition', 'eWORDTYPE_ADDED',
    'SpeechGrammarTagUnlimitedDictation',
    'DISPID_SVAllowAudioOuputFormatChangesOnNextSet', 'SPRULE',
    'SpeechCategoryRecoProfiles', 'SVSFParseMask', 'ISpPhraseAlt',
    'WAVEFORMATEX', 'ISpVoice', 'SPRST_NUM_STATES', 'SPLO_DYNAMIC',
    'SPSNotOverriden', 'DISPID_SAFSetWaveFormatEx', 'SVP_15',
    'SpeechVisemeType', 'SRERecognition', 'DISPID_SOTGetDescription',
    'DISPID_SPERetainedSizeBytes', 'DISPID_SPRsItem',
    'eLEXTYPE_PRIVATE15', 'SPRECOCONTEXTSTATUS',
    'SECNormalConfidence', 'SSFMOpenReadWrite',
    'DISPID_SGRSTNextState', 'DISPID_SRGCmdLoadFromFile',
    'SAFT32kHz8BitStereo', 'DISPID_SpeechPhoneConverter',
    'DISPID_SRGCmdLoadFromResource', 'SAFT16kHz8BitStereo',
    'SPEI_FALSE_RECOGNITION', 'DISPID_SPILanguageId',
    'DISPID_SOTCategory', 'ISpeechPhraseInfoBuilder',
    'DISPID_SOTCDefault', 'SPAO_NONE', 'SAFTCCITT_ALaw_22kHzMono',
    'SDA_One_Trailing_Space', 'SpeechRecognizerState',
    'eLEXTYPE_MORPHOLOGY', 'DISPID_SLRemovePronunciationByPhoneIds',
    '_ISpeechVoiceEvents', 'DISPID_SPIStartTime', 'SVP_12',
    'DISPID_SRCResume', 'ISpeechRecognizer', 'SDTAlternates',
    'SPEI_RESERVED6', 'SPEI_MIN_TTS', 'DISPID_SWFEAvgBytesPerSec',
    'SAFT16kHz16BitMono', 'DISPID_SPISaveToMemory', 'SPSHT_Unknown',
    'DISPID_SPIRule', 'DISPID_SPEAudioTimeOffset', 'SITooSlow',
    'SPSMF_UPS', 'SLTUser', 'SWTAdded', 'DISPID_SpeechWaveFormatEx',
    'DISPID_SRCVoice', 'SP_VISEME_13', 'SVP_13',
    'DISPID_SRCEPhraseStart', 'ISpGrammarBuilder',
    'ISpeechRecoResultDispatch', 'SP_VISEME_9', 'SPSHT_NotOverriden',
    'SSTTTextBuffer', 'SPBINARYGRAMMAR', 'SPEI_MAX_TTS',
    'DISPID_SGRAddState', 'DISPID_SDKEnumKeys', 'DISPID_SPRuleName',
    'DISPIDSPTSI_SelectionOffset', 'ISpStream', 'ISpeechBaseStream',
    'SAFT12kHz16BitMono', 'IStream', 'SPSHORTCUTPAIRLIST',
    'SGSExclusive', 'DISPID_SDKEnumValues', 'SpeechEngineConfidence',
    'SpStreamFormatConverter', 'DISPID_SASCurrentDevicePosition',
    'ISpeechObjectToken', 'SPTEXTSELECTIONINFO', 'SASStop',
    'SPRST_INACTIVE', 'SINoise', 'DISPID_SVAudioOutput',
    'DISPID_SRCBookmark', 'SAFT12kHz8BitMono', 'SDTLexicalForm',
    'eLEXTYPE_RESERVED10', 'DISPID_SVIsUISupported',
    'IInternetSecurityManager', 'DISPID_SLAddPronunciationByPhoneIds',
    'SVF_Emphasis', 'DISPID_SVSLastBookmark', 'SAFT8kHz16BitMono',
    'SAFT32kHz16BitMono', 'SVSFIsFilename', 'SASRun',
    'SRTExtendableParse', 'DISPID_SASFreeBufferSpace', 'eLEXTYPE_APP',
    'SPSFunction', 'DISPID_SRCCreateResultFromMemory', 'SPWT_LEXICAL',
    'SFTInput', 'SPBO_TIME_UNITS', 'SPVPRI_ALERT',
    'DISPID_SASCurrentSeekPosition', 'DISPID_SLPType',
    'SGRSTTWildcard', '_RemotableHandle', 'SRAONone',
    'SpCompressedLexicon', 'DISPID_SPEDisplayText',
    'SAFTNonStandardFormat', 'SDTRule',
    'DISPID_SRSCurrentStreamNumber', 'SPSInterjection', 'SPSHT_EMAIL',
    'SPWF_SRENGINE', 'DISPID_SVEViseme', 'SpeechRecognitionType',
    'SRSInactiveWithPurge', 'DISPID_SFSClose', 'SRSEDone',
    'DISPID_SAFGuid', 'DISPID_SGRsItem', 'SP_VISEME_2', 'SPAR_Low',
    'IEnumSpObjectTokens', 'SpeechPropertyResponseSpeed', 'SVSFIsXML',
    'ISpeechXMLRecoResult', 'SVEViseme', 'SpeechGrammarState',
    'SAFTTrueSpeech_8kHz1BitMono', 'SpResourceManager',
    'DISPID_SVEStreamStart', 'SDTAudio', 'SPEVENT',
    'SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE', 'SPGS_DISABLED',
    'SPPS_Noncontent', 'DISPID_SVSInputSentenceLength',
    'SpObjectToken', 'SVSFVoiceMask', 'eLEXTYPE_PRIVATE18',
    'SPSHT_OTHER', 'SP_VISEME_8', 'DISPID_SpeechPhraseReplacements',
    'SpeechDataKeyLocation', 'SpeechTokenContext', 'SPEI_VISEME',
    'SPDKL_DefaultLocation', 'SPBO_PAUSE', 'DISPID_SVEWord',
    'DISPID_SpeechRecognizer', 'DISPID_SPANumberOfElementsInResult',
    'SPPARTOFSPEECH', 'SPAUDIOOPTIONS',
    'DISPID_SPIGetDisplayAttributes', 'ISpeechPhraseReplacement',
    'SVP_4', 'SAFTCCITT_uLaw_44kHzMono', 'Speech_Max_Pron_Length',
    'SpeechRegistryLocalMachineRoot', 'SDTProperty',
    'SPWT_LEXICAL_NO_SPECIAL_CHARS', 'DISPID_SPIAudioStreamPosition',
    'SSSPTRelativeToEnd', 'DISPID_SpeechPhraseElements',
    'SAFTCCITT_ALaw_8kHzStereo', 'ISpShortcut', 'DISPID_SRGId',
    'DISPID_SGRSAddWordTransition', 'SpMMAudioEnum',
    'SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN', 'STCRemoteServer',
    'SGDSActiveWithAutoPause', 'SVEStartInputStream',
    'SpeechVoiceEvents', 'SpeechTokenValueCLSID', 'SP_VISEME_5',
    'DISPID_SVStatus', 'SRCS_Enabled', 'DISPID_SPIProperties',
    'ISpRecoGrammar2', 'ISpeechObjectTokenCategory', 'SINone',
    'DISPID_SRRecognizer', 'DISPID_SRCEventInterests',
    'DISPID_SPRuleId', 'SPSSuppressWord', 'DISPIDSPRG', 'SPWORDTYPE',
    'DISPID_SpeechPhraseRules', 'SVP_18', 'SPWF_INPUT', 'SLOStatic',
    'DISPID_SRRDiscardResultInfo', 'DISPID_SpeechAudioFormat',
    'DISPID_SGRSAddRuleTransition', 'SPINTERFERENCE_TOOQUIET',
    'DISPID_SOTRemoveStorageFileName', 'SpeechRegistryUserRoot',
    'DISPID_SVWaitUntilDone', 'ISpeechGrammarRuleStateTransitions',
    'ISpeechMMSysAudio', 'SGLexicalNoSpecialChars',
    'SPSERIALIZEDRESULT', 'SPWORDLIST', 'ISpeechAudioFormat',
    'DISPID_SMSGetData', 'DISPID_SPPs_NewEnum', 'DISPID_SRDisplayUI',
    'DISPID_SRCERecognition', 'SPSHORTCUTPAIR', 'DISPID_SWFEChannels',
    'DISPID_SGRsCommitAndSave', 'SAFTCCITT_ALaw_44kHzStereo',
    'SPPS_NotOverriden', 'DISPID_SLGetWords',
    'DISPID_SLAddPronunciation', 'ISpeechGrammarRuleState',
    'SpeechBookmarkOptions', 'DISPID_SPAsItem',
    'DISPID_SOTIsUISupported', 'SPWT_PRONUNCIATION', 'ISpAudio',
    '_SPAUDIOSTATE', 'DISPID_SGRsDynamic', 'SpAudioFormat',
    'SPRST_ACTIVE', 'DISPID_SPPBRestorePhraseFromMemory',
    'DISPID_SOTCId', 'ISpeechTextSelectionInformation',
    'ISpeechPhraseElement', 'eLEXTYPE_USER_SHORTCUT',
    'eLEXTYPE_PRIVATE17', 'ISpDataKey', 'DISPID_SRSetPropertyNumber',
    'DISPID_SGRsFindRule', 'SPPHRASEPROPERTY', 'SVP_14',
    'SAFTCCITT_ALaw_8kHzMono', 'DISPIDSPTSI_ActiveLength',
    'SpeechVoicePriority', 'SpeechVisemeFeature', 'SpLexicon',
    'DISPID_SGRSTsCount', 'DISPID_SPIGrammarId',
    'ISpNotifyTranslator', 'DISPID_SRRRecoContext',
    'DISPID_SpeechCustomStream', 'SINoSignal',
    'DISPID_SpeechPhraseReplacement', 'SP_VISEME_4',
    'eLEXTYPE_RESERVED4', 'SpCustomStream', 'SpeechAllElements',
    'ISpLexicon', 'DISPID_SLWs_NewEnum', 'DISPID_SOTCEnumerateTokens',
    'DISPID_SPIAudioSizeTime', 'SVP_0', 'SpeechDisplayAttributes',
    'SPSUnknown', 'DISPID_SRGRules', 'DISPID_SRCRecognizer',
    'SAFT44kHz16BitMono', 'SpSharedRecognizer',
    'SpeechWordPronounceable', 'DISPID_SRCEBookmark',
    'DISPID_SRGDictationLoad', 'DISPID_SpeechLexiconPronunciation',
    'DISPID_SVSLastStreamNumberQueued', 'SRCS_Disabled',
    'SGDSInactive', 'DISPID_SPRText', 'SAFTCCITT_ALaw_11kHzMono',
    'SpeechGrammarTagWildcard', 'SPAUDIOSTATE',
    'SAFTGSM610_22kHzMono', 'eLEXTYPE_PRIVATE6', 'SPGS_EXCLUSIVE',
    'SECHighConfidence', 'SPPS_Interjection', 'DISPID_SPELexicalForm',
    'SpeechDictationTopicSpelling', 'SPSERIALIZEDPHRASE', 'SBOPause',
    'DISPID_SRGSetTextSelection', 'DISPID_SPACommit', 'SP_VISEME_7',
    'DISPID_SREmulateRecognition', 'SP_VISEME_10', 'SPAUDIOSTATUS',
    'SAFT24kHz16BitMono', 'SAFTADPCM_8kHzMono',
    'DISPID_SpeechRecognizerStatus', 'Speech_Default_Weight',
    'SP_VISEME_21', 'STSF_CommonAppData',
    'DISPID_SRCAudioInInterferenceStatus', 'SVEPrivate',
    'DISPID_SGRSTType', 'SpInProcRecoContext',
    'tagSPTEXTSELECTIONINFO', 'DISPID_SOTsCount',
    'SPFM_OPEN_READONLY', 'SPEI_SR_AUDIO_LEVEL',
    'SAFTNoAssignedFormat', 'SAFTCCITT_ALaw_11kHzStereo',
    'SpeechCategoryVoices', 'DISPID_SPAStartElementInResult',
    'SREHypothesis', 'DISPID_SpeechRecoResult2',
    'DISPID_SPRNumberOfElements', 'DISPID_SpeechMMSysAudio',
    'SAFT16kHz8BitMono', 'SPFM_CREATE_ALWAYS',
    'DISPID_SRCreateRecoContext', 'DISPID_SVEStreamEnd',
    'SECFIgnoreKanaType', 'SPWORDPRONUNCIATIONLIST',
    'ISpeechMemoryStream', 'DISPID_SPRuleConfidence',
    'SpWaveFormatEx', 'DISPID_SLWsCount', 'eLEXTYPE_PRIVATE12',
    'SPWT_DISPLAY', 'DISPID_SpeechObjectToken', 'DISPID_SRCState',
    'SRESoundEnd', 'ISpRecognizer', '_ISpeechRecoContextEvents',
    'SpNotifyTranslator', 'SVSFDefault', 'SDTReplacement',
    'SAFTCCITT_uLaw_11kHzMono', 'DISPID_SRGetPropertyString',
    'SREFalseRecognition', 'SPAR_Medium',
    'DISPID_SRSNumberOfActiveRules', 'SPCT_COMMAND',
    'DISPID_SRRTTickCount', 'SAFT8kHz8BitStereo',
    'SAFT48kHz16BitMono', 'ISpRecognizer2', 'DISPID_SVSLastResult',
    'ISpeechRecoContext', 'DISPID_SGRSAddSpecialTransition',
    'SPCATEGORYTYPE', 'DISPID_SOTDisplayUI', 'SPPS_RESERVED4',
    'SPVISEMES', 'SVSFNLPSpeakPunc',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_MS', 'ISpeechPhraseInfo',
    'SRAExport', 'SVPNormal', 'SPAO_RETAIN_AUDIO', 'SECFDefault',
    'SITooFast', 'SPEI_MIN_SR', 'DISPID_SPIGetText',
    'SAFT8kHz16BitStereo', 'DISPID_SpeechAudioStatus',
    'SPEI_WORD_BOUNDARY', 'SGPronounciation', 'ISpeechPhraseRule',
    'STSF_AppData', 'SVSFNLPMask', 'SWTDeleted',
    'ISpeechPhraseProperty', 'DISPID_SPERequiredConfidence',
    'eLEXTYPE_USER', 'DISPID_SVDisplayUI', 'SPVPRI_NORMAL',
    'ISpeechPhraseAlternate', 'SRSActive', 'SAFT11kHz16BitStereo',
    'SpVoice', 'SLODynamic', 'SPPS_RESERVED1', 'ISpeechVoiceStatus',
    'SVEAllEvents', 'DISPID_SVSInputWordPosition',
    'DISPID_SVGetVoices', 'DISPID_SRCEEndStream',
    'DISPID_SpeechGrammarRuleStateTransitions', 'SP_VISEME_3',
    'SPRS_INACTIVE', 'SVESentenceBoundary', 'DISPID_SDKDeleteValue',
    'DISPID_SPRs_NewEnum', 'DISPID_SLPs_NewEnum',
    'SpeechPartOfSpeech', 'DISPID_SPERetainedStreamOffset',
    'SPPS_Noun', 'DISPID_SRAudioInput',
    'DISPID_SRSSupportedLanguages', 'DISPID_SVSyncronousSpeakTimeout',
    'ISpeechRecoGrammar', 'ISpeechLexicon', 'DISPID_SVSVisemeId',
    'SPEI_RECO_OTHER_CONTEXT', 'SREPropertyStringChange',
    'DISPID_SPPsCount', 'DISPID_SRRTLength',
    'SPRS_ACTIVE_USER_DELIMITED', 'DISPID_SRRSaveToMemory',
    'SPINTERFERENCE_TOOSLOW', 'DISPID_SOTGetStorageFileName',
    'DISPID_SPIRetainedSizeBytes', 'DISPID_SpeechObjectTokens',
    'SDA_No_Trailing_Space', 'STSF_LocalAppData', 'SVEAudioLevel',
    'SpNullPhoneConverter', 'DISPID_SVPriority',
    'SpeechRecoContextState', 'DISPID_SpeechPhraseBuilder',
    'SPBO_NONE', 'DISPID_SLGenerationId', 'SP_VISEME_12',
    'DISPID_SOTMatchesAttributes', 'SpMMAudioOut', 'SRAORetainAudio',
    'DISPID_SOTDataKey', 'ISpeechGrammarRule', 'DISPID_SDKDeleteKey',
    'DISPID_SPIReplacements', 'SpeechAddRemoveWord',
    'DISPID_SLWPronunciations', 'SPLOADOPTIONS',
    'DISPID_SRCEAdaptation', 'DISPID_SPPNumberOfElements',
    'SAFTCCITT_ALaw_44kHzMono', 'DISPID_SPPEngineConfidence',
    'DISPID_SpeechGrammarRuleState', 'SP_VISEME_0',
    'SpeechInterference', 'eLEXTYPE_PRIVATE16', 'SPRST_ACTIVE_ALWAYS',
    'DISPID_SPIAudioSizeBytes', 'SPEI_SOUND_END',
    'DISPID_SVSCurrentStreamNumber', 'SVP_16',
    'SGDSActiveUserDelimited', 'SPRECORESULTTIMES',
    'DISPID_SAFGetWaveFormatEx', 'DISPID_SGRClear',
    'DISPID_SVEBookmark', 'DISPID_SVPause', 'SpeechRecoEvents',
    'DISPID_SRRTOffsetFromStart', 'SpeechPropertyResourceUsage',
    'SVP_11', 'DISPID_SPRulesItem', 'SPEI_RECOGNITION',
    'DISPID_SRCERequestUI', 'SpeechFormatType', 'SpeechAudioState',
    'ISpRecoCategory', 'DISPID_SABufferInfo', 'ISpeechWaveFormatEx',
    'SAFT22kHz8BitStereo', 'SPSEMANTICFORMAT',
    'SpeechPropertyComplexResponseSpeed', 'SAFTADPCM_22kHzStereo',
    'SpeechEngineProperties', 'ISpeechVoice', 'SAFT16kHz16BitStereo',
    'ISpEventSink', 'SpeechCategoryRecognizers', 'SVPAlert',
    'DISPID_SVGetAudioOutputs', 'DISPID_SpeechAudio', 'SP_VISEME_14',
    'SPEI_PHRASE_START', 'SSTTDictation', 'SpUnCompressedLexicon',
    'SPPROPERTYINFO', 'DISPID_SpeechXMLRecoResult', 'SpeechRuleState',
    'SGRSTTDictation', 'SDTDisplayText', 'SAFTADPCM_8kHzStereo',
    'eLEXTYPE_PRIVATE11', 'SPCT_SLEEP', 'SPPS_LMA',
    'DISPID_SGRSTWeight', 'DISPID_SMSAMMHandle', 'SPPHRASERULE',
    'DISPID_SGRSTs_NewEnum', 'eLEXTYPE_PRIVATE7',
    'DISPID_SVAlertBoundary', 'DISPID_SRAudioInputStream',
    'SPFM_OPEN_READWRITE', 'DISPID_SRCRequestedUIType',
    'SpeechMicTraining', 'Speech_StreamPos_RealTime',
    'DISPID_SRGCmdSetRuleState', 'SpFileStream', 'SRERequestUI',
    'DISPID_SRCPause', 'DISPID_SPEPronunciation',
    'DISPID_SWFESamplesPerSec', 'DISPID_SVGetProfiles',
    'DISPID_SRRSpeakAudio', 'DISPID_SPRDisplayAttributes',
    'SPEVENTSOURCEINFO', 'DISPID_SBSSeek',
    'DISPIDSPTSI_SelectionLength', 'SRSEIsSpeaking',
    'SPEI_SR_RETAINEDAUDIO', 'SPEI_RESERVED3', 'ISpeechDataKey',
    'SPEI_RESERVED2', 'DISPID_SPRuleParent', 'SRSActiveAlways',
    'SPPS_Modifier', 'SPRST_INACTIVE_WITH_PURGE',
    'DISPID_SPCIdToPhone', 'SPEI_TTS_AUDIO_LEVEL',
    'DISPID_SDKOpenKey', 'SPPS_Unknown', 'SPPS_SuppressWord',
    'SPSLMA', 'SpeechVoiceCategoryTTSRate', 'DISPID_SPRules_NewEnum',
    'DISPID_SLWLangId', 'DISPID_SpeechPhraseInfo', 'SREStreamStart',
    'SPPS_Function', 'DISPID_SWFEBitsPerSample', 'DISPID_SGRName',
    'ISpXMLRecoResult', 'DISPID_SpeechRecoResultTimes',
    '__MIDL___MIDL_itf_sapi_0000_0020_0002',
    'DISPID_SVGetAudioInputs', 'STCAll', 'SBONone', 'SGDSActive',
    'eWORDTYPE_DELETED', 'DISPID_SRSetPropertyString',
    'SECFIgnoreWidth', 'SpeechRecoProfileProperties',
    'SPEI_PROPERTY_NUM_CHANGE', 'DISPID_SpeechBaseStream',
    'SPDKL_CurrentUser', 'SpeechAudioVolume', 'SRADefaultToActive',
    'DISPID_SPPId', 'DISPID_SLPsCount', 'ISpeechResourceLoader',
    'SSFMCreateForWrite', 'DISPID_SPRuleNumberOfElements',
    'SpeechTokenKeyUI', 'DISPID_SRStatus',
    'DISPID_SRGIsPronounceable', 'DISPID_SRRGetXMLResult',
    'ISpeechLexiconWords', 'SpeechAudioProperties',
    'SPBOOKMARKOPTIONS', 'DISPID_SpeechPhraseProperty',
    'DISPID_SRRTStreamTime', 'SPGRAMMARWORDTYPE',
    'DISPID_SRGCmdLoadFromProprietaryGrammar', 'SpPhoneConverter',
    'DISPID_SRRPhraseInfo', 'SPRECOGNIZERSTATUS', 'SPGRAMMARSTATE',
    'SWPKnownWordPronounceable', 'DISPID_SOTCreateInstance',
    'DISPID_SRRAudioFormat', 'SREBookmark', 'SPEI_RESERVED1',
    'SpeechGrammarTagDictation', 'DISPID_SGRSTsItem',
    'SAFTCCITT_uLaw_22kHzStereo', 'DISPID_SRRSetTextFeedback',
    'SDA_Two_Trailing_Spaces', 'SPEI_PROPERTY_STRING_CHANGE',
    'SPCS_DISABLED', 'SAFTCCITT_uLaw_22kHzMono',
    'DISPID_SRSCurrentStreamPosition', 'ISpRecoGrammar',
    'SpObjectTokenCategory', 'SGLexical', 'DISPID_SLPSymbolic',
    'SpMMAudioIn', 'SPAR_High', 'DISPID_SRRAlternates',
    'SAFT32kHz8BitMono', 'ISpRecoContext2',
    'SpeechPropertyHighConfidenceThreshold', 'SPPS_RESERVED2',
    'ISpeechPhraseReplacements', 'ISpNotifySource', 'ISpMMSysAudio',
    'ISpeechLexiconWord', 'SVP_21', 'SpeechTokenKeyFiles',
    'SRTEmulated', 'eLEXTYPE_PRIVATE20', 'DISPID_SGRSTRule',
    'DISPID_SDKSetStringValue', 'DISPID_SPPsItem',
    'eLEXTYPE_RESERVED7', 'DISPID_SWFEBlockAlign', 'SP_VISEME_17',
    'SPINTERFERENCE_NOISE', 'eLEXTYPE_PRIVATE9', 'SPPS_RESERVED3',
    'DISPID_SpeechPhraseRule', 'SPAR_Unknown', 'DISPID_SRProfile',
    'SPEI_VOICE_CHANGE', 'SP_VISEME_15', 'SP_VISEME_18', 'SVP_17',
    'SP_VISEME_19', 'DISPID_SRGSetWordSequenceData',
    'SpTextSelectionInformation', 'SPAS_RUN',
    'DISPIDSPTSI_ActiveOffset', 'DISPID_SGRSTPropertyName',
    'SpeechCategoryPhoneConverters', 'DISPID_SOTId',
    'DISPID_SPPConfidence', 'SVF_Stressed',
    'DISPID_SpeechObjectTokenCategory', 'DISPID_SPEsCount',
    'ISpeechCustomStream', 'Speech_Max_Word_Length',
    'DISPID_SPEAudioSizeTime', 'DISPID_SRIsShared', 'SRTStandard',
    'SAFTGSM610_44kHzMono',
    'DISPID_SRAllowAudioInputFormatChangesOnNextSet',
    'DISPID_SPPChildren', 'DISPID_SWFEExtraData',
    'SAFTADPCM_11kHzStereo', 'DISPID_SLPLangId',
    'DISPID_SGRSTPropertyValue', 'ISpeechAudio', 'DISPID_SRGetFormat'
]

