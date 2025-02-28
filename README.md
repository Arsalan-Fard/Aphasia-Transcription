# Aphasia-Transcription

## 1. Non-Speech Markers in Transcription

## 1.1 CHAT Transcription Postcodes

| Letters  | Categories                | Example          | Meaning                  | POS       |
|----------|---------------------------|------------------|--------------------------|-----------|
| @b       | Babbling                   | abame@b         | -                        | bab       |
| @c       | Child-invented form        | gumma@c         | sticky                   | chi       |
| @d       | Dialect form               | younz@d         | you                      | dia       |
| @f       | Family-specific form       | bunko@f         | broken                   | fam       |
| @fp      | Filled pause               | um@fp           | use &-um instead         | skip      |
| @g       | General special form       | gongga@g        | -                        | skip      |
| @i       | Interjection, interaction  | huhuh@i         | -                        | co        |
| @k       | Multiple letters           | abcd@k          | abcd                     | n:let     |
| @l       | Letter                     | b@l             | letter b                 | n:let     |
| @n       | Neologism                  | breaked@n       | broke                    | neo       |
| @o       | Onomatopoeia               | woofwoof@o      | dog barking              | on        |
| @p       | Phonological consistent form | aga@p        | -                        | phon      |
| @q       | Metalinguistic use         | no if@q-s but@q-s | when citing words      | meta      |
| @s:*     | Second-language form       | istenem@s:hu    | Hungarian word           | L2        |
| @s$n     | Second-language noun       | perro@s$n       | Spanish noun             | n         |
| @si      | Singing                    | lalala@si       | singing                  | sing      |
| @sl      | Signed language            | apple@sl        | signs apple              | sign      |
| @sas     | Sign & speech              | apple@sas       | signs and says apple     | sas       |
| @w       | Test word                  | wug@w           | test word                | wug       |
| @u       | Unibet transcription       | binga@u         | -                        | uni       |
| @wp      | Word play                  | goobarumba@wp   | -                        | wp        |
| @x       | Excluded words             | stuff@x         | -                        | unk       |
| @z:xxx   | User-defined code          | word@z:rtfd     | any user code            | -         |


## 1.2 Shortenings

<table>
  <tr>
    <th colspan="4" style="text-align:center;">Examples of Shortenings</th>
  </tr>
  <tr>
    <td>(a)bout</td>
    <td>don('t)</td>
    <td>(h)is</td>
    <td>(re)frigerator</td>
  </tr>
  <tr>
    <td>an(d)</td>
    <td>(e)nough</td>
    <td>(h)isself</td>
    <td>(re)member</td>
  </tr>
  <tr>
    <td>(a)n(d)</td>
    <td>(e)spress(o)</td>
    <td>-in(g)</td>
    <td>sec(ond)</td>
  </tr>
  <tr>
    <td>(a)fraid</td>
    <td>(e)spresso</td>
    <td>nothin(g)</td>
    <td>s(up)pose</td>
  </tr>
  <tr>
    <td>(a)gain</td>
    <td>(es)press(o)</td>
    <td>(i)n</td>
    <td>(th)e</td>
  </tr>
  <tr>
    <td>(a)nother</td>
    <td>(ex)cept</td>
    <td>(in)stead</td>
    <td>(th)em</td>
  </tr>
  <tr>
    <td>(a)round</td>
    <td>(ex)cuse</td>
    <td>Jag(uar)</td>
    <td>(th)emselves</td>
  </tr>
  <tr>
    <td>ave(nue)</td>
    <td>(ex)cused</td>
    <td>lib(r)ary</td>
    <td>(th)ere</td>
  </tr>
  <tr>
    <td>(a)way</td>
    <td>(e)xcuse</td>
    <td>Mass(achusetts)</td>
    <td>(th)ese</td>
  </tr>
  <tr>
    <td>(be)cause</td>
    <td>(e)xcused</td>
    <td>micro(phone)</td>
    <td>(th)ey</td>
  </tr>
  <tr>
    <td>(be)fore</td>
    <td>(h)e</td>
    <td>(pa)jamas</td>
    <td>(to)gether</td>
  </tr>
  <tr>
    <td>(be)hind</td>
    <td>(h)er</td>
    <td>(o)k</td>
    <td>(to)mato</td>
  </tr>
  <tr>
    <td>b(e)long</td>
    <td>(h)ere</td>
    <td>o(v)er</td>
    <td>(to)morrow</td>
  </tr>
  <tr>
    <td>b(e)longs</td>
    <td>(h)erself</td>
    <td>(po)tato</td>
    <td>(to)night</td>
  </tr>
  <tr>
    <td>Cad(illac)</td>
    <td>(h)im</td>
    <td>prob(ab)ly</td>
    <td>(un)til</td>
  </tr>
  <tr>
    <td>doc(tor)</td>
    <td>(h)imself</td>
    <td>(re)corder</td>
    <td>wan(t)</td>
  </tr>
</table>


## 1.3 Other Types of Signs in CHAT

| Type of Sign                 | Example(s)                          | Description |
|------------------------------|-------------------------------------|-------------|
| **Simple Events**            | &=laughs, &=sneezes, &=yells        | Short non-verbal events occurring at a point in speech. |
| **Imitations**               | &=imit:motor, &=imit:lion          | Vocal imitations of sounds (e.g., animal sounds, engine sounds). |
| **Gestures**                 | &=ges:frustration, &=ges:ignore    | Non-verbal gestures indicating emotions or actions. |
| **Actions on Objects**       | &=writes:dog, &=points:car         | Actions performed on objects, such as pointing, writing, or showing. |
| **Body Movements**           | &=head:yes, &=mouth:open           | Body movements, including nodding, shaking, opening/closing eyes, etc. |
| **Interposed Word**          | &*MOT:mhm                          | A word inserted by another speaker into the current speaker’s utterance. |
| **Complex Local Events**     | [^ text]                           | Open-form descriptions of local events at a specific point. |
| **Pauses**                   | (.), (..), (...)                   | Silent pauses of increasing duration. |
| **Timed Pauses**             | (0.15), (1:05.15)                  | Pauses measured in seconds or minutes. |
| **Long Vocal Events**        | &{l=laughs ... &}l=laughs          | Extended vocal events such as laughter over a duration. |
| **Long Non-Vocal Events**    | &{n=waving:hands ... &}n=waving:hands | Extended non-verbal events such as hand-waving. |
| **Trailing Off**             | +...                                | Incomplete utterance where the speaker trails off. |
| **Trailing Off Question**    | +..?                                | An incomplete question where the speaker trails off. |
| **Question with Exclamation**| +!?                                 | A question with strong emphasis or amazement. |
| **Interruption**             | +/.                                 | An incomplete utterance due to interruption by another speaker. |
| **Interrupted Question**     | +/?                                 | An interrupted question. |
| **Self-Interruption**        | +//.                                | A speaker interrupts their own utterance to start a new one. |
| **Self-Interrupted Question**| +//?                                | A self-interrupted utterance in the form of a question. |
| **Transcription Break**      | +.                                  | A phrase boundary marking overlap. |
| **Quotation Notation**       | +"/., +"., +", " "                 | Indicates quoted material in speech. |
| **Quick Uptake**             | +^                                  | A fast response without a typical pause. |
| **Self-Completion**          | +,                                  | A speaker completes their own interrupted utterance. |
| **Other Completion**         | ++                                  | A second speaker completes another speaker’s utterance. |
| **Explanations**              | [= closet]                           | Brief explanation about a word or phrase in the text. |
| **Replacement**               | whyncha [: why don’t you]            | Replaces a nonstandard word with its standard equivalent for analysis. |
| **Real Word Replacement**      | piece [:: peach] [*]                 | Used when a real word is incorrectly used instead of another real word. |
| **Alternative Transcription**  | <one or two> [=? one too]            | Indicates an alternative possible transcription of the phrase. |
| **Comment on Main Line**       | [% said with strong raising of eyebrows] | Allows for an in-line comment rather than a separate annotation. |
| **Best Guess**                | frog [?]                             | Indicates uncertainty in transcription due to unclear audio. |
| **Overlap Follows**           | <stop doing that> [>]                | Marks where the speaker’s utterance overlaps with another speaker’s speech. |
| **Overlap Precedes**          | <Mommy I don’t like this> [<]        | Indicates that the utterance is overlapping with the preceding speaker’s speech. |
| **Lazy Overlap**              | +<                                    | Marks an overlap without specifying its exact duration. |
| **Repetition**                | <I wanted> [/] I wanted              | The speaker repeats a word or phrase without correction. |
| **Retracing**                 | <I wanted> [//] I thought I wanted   | A speaker restarts a phrase with some corrections. |
| **Reformulation**             | <all of my friends had> [///] we all decided | A complete reformulation of the message without simple correction. |
| **False Start Without Retracing** | <I wanted> [/-] uh when is Margie coming? | Marks a false start where the speaker abandons the phrase entirely. |
| **Unclear Retracing Type**    | [/?]                                 | Used when reformatting SALT files into CHAT format where retracings are ambiguous. |
| **Excluded Material**         | <I think that maybe> [e]             | Marks material that should be excluded from certain analyses. |
| **Clause Delimiter**          | [^c]                                 | Used to segment complex utterances into clauses. |
| **Error Marking**             | goed [: went] [*]                    | Marks an error in word usage along with its correction. |
| **Precodes (Language Switch)** | [- spa]                              | Marks a language switch in multilingual transcriptions. |
| **Postcodes (Utterance-Level Tags)** | not this one. [+ neg] [+ req] [+ inc] | Customizable codes applied to entire utterances. |
| **Excluded Utterance**        | just a moment. [+ bch]               | Marks utterances that should be excluded from analysis (e.g., background talk). |
| **Included Utterance**        | 0. [+ trn]                           | Marks nonverbal utterances as turns for analysis. |
| **[+ gram]** | wented [+ gram] | Marks a **grammatical error** in speech. |
| **[+ per]** | I, I, I, I want it [+ per] | Indicates **perseveration**, where a word or phrase is **repeated excessively** beyond what is necessary. |
| **[+ jar]** | blarfamadoo [+ jar] | Identifies **jargon**, speech that consists of **meaningless or unintelligible words**. |
| **[+ cir]** | the thing that you use to eat soup [+ cir] | Marks **circumlocution**, where a speaker **describes** something instead of using the correct term. |
| **[+ es]** | uh, um, you know, well [+ es] | Indicates **empty speech**, which consists of **filler words or phrases** that do not add meaningful content. |


Reference: Tools for Analyzing Talk, Part 1: The CHAT Transcription Format, Brian MacWhinney, Carnegie Mellon University

## 2. Word Error Rate (WER) improvement

- Whispers
- ASsembly
- LLM

## 3. Code for Human Analysis of Transcript (CHAT)

### 3.1 Diarization
### 3.2 
Activity detection?!


