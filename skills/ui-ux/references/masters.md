# Principles of the masters

What the suite takes from the classics. Each rule has a check question and a case. Applies to all
sub-skills; name the term in findings so it can be looked up.

## Read the originals

- Don Norman: [The Design of Everyday Things](https://www.nngroup.com/books/design-everyday-things-revised/)
  (revised edition 2013), [Signifiers, not affordances](https://jnd.org/signifiers-not-affordances/),
  [Affordances and design](https://jnd.org/affordances-and-design/),
  [The Two UX Gulfs](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/),
  [Mapping](https://www.interaction-design.org/literature/topics/mapping)
- Jakob Nielsen: [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/),
  [Consistency and Standards](https://www.nngroup.com/articles/consistency-and-standards/),
  [Aesthetic and Minimalist Design](https://www.nngroup.com/articles/aesthetic-minimalist-design/),
  [Toggle-Switch Guidelines](https://www.nngroup.com/articles/toggle-switch-guidelines/)
- Gestalt: [Principles of grouping](https://en.wikipedia.org/wiki/Principles_of_grouping),
  [Proximity](https://www.nngroup.com/articles/gestalt-proximity/),
  [Similarity](https://www.nngroup.com/articles/gestalt-similarity/),
  [Principles of Visual Design](https://www.nngroup.com/articles/principles-visual-design/),
  [Cumulative Layout Shift](https://web.dev/articles/cls)
- UX writing: Ginny Redish, [Letting Go of the Words](https://shop.elsevier.com/books/letting-go-of-the-words/redish/978-0-12-385930-3),
  [Writing for GOV.UK](https://www.gov.uk/guidance/content-design/writing-for-gov-uk),
  [How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/),
  [UI Copy](https://www.nngroup.com/articles/ui-copy/)

## 1. Interaction (Norman)

| Term | Meaning | Check question |
|---|---|---|
| **Signifier** (affordance) | The element shows that and how it can be used | Does it invite use, and only when it actually does something? |
| **Mapping** | Control and effect belong together spatially | Is the effect visible where the user acted? |
| **Feedback** | Every action gets an immediate visible answer | What has visibly changed after the click? |
| **Gulf of execution** | Gap between "I want to" and "I know how" | Can the action be found without help? |
| **Gulf of evaluation** | Gap between "I did it" and "I see what happened" | Is the new state recognisable without thinking? |
| **Conceptual model** | The picture in the user's head of how the system works | Does what happens match what the label promises? |
| **Constraints** | Wrong input is impossible in the first place | Can the mistake be made, instead of being reported afterwards? |

**Basement switch.** A switch whose effect happens elsewhere is like a light switch in the basement
that turns on the attic light: it invites flipping, and then one wonders what happened. If a setting
acts outside the page, the label names the place ("Show in lists") and the help text says where the
effect can be seen, ideally with a link there. Case: a settings toggle "Show examples" that only
changes lists on other pages.

## 2. Heuristics (Nielsen)

| # | Heuristic | Short form |
|---|---|---|
| 1 | Visibility of system status | Loading, saving, state always visible (`ui-ux-passive`) |
| 2 | Match with the real world | Terms from the users' work, order as on paper |
| 3 | User control and freedom | Undo, cancel, trash (`ui-ux-active`) |
| 4 | **Consistency and standards** | The same looks the same and stays in the same place |
| 5 | Error prevention | Constraints before messages |
| 6 | Recognition rather than recall | Choice instead of free input, keep context visible |
| 7 | Flexibility and efficiency | Keyboard, remembered filters, shortcuts for experts |
| 8 | **Aesthetic and minimalist design** | Every word and element must earn its place |
| 9 | Recognise, diagnose, recover from errors | Problem + solution, warning with a way out |
| 10 | Help and documentation | A help page per flow |

**Stable frame** (heuristic 4). Header, menu and side navigation stay in place when the user switches
a tab or opens a page. If the frame disappears on one page, space appears that was not there before.
It works like contrast: the eye jumps there and looks for a meaning that does not exist. Check
question: is the frame the same on every tab? Case: one tab of a settings page suddenly showing no
menu.

## 3. Perception (Gestalt)

| Law | Meaning | Check question |
|---|---|---|
| **Proximity** | What is close together belongs together | Do the spacing steps (tokens) reflect what belongs together? |
| **Similarity** | What looks alike seems alike | Do alike things look alike and different things different? |
| **Figure and ground** | White space is not a remainder, it shapes the figure | Is the white space intended, or did something drop out? |
| **Closure / common region** | Containers hold groups | Is the border needed, or does spacing suffice? |
| **Contrast** | Difference draws the eye | Does the strongest contrast point to the most important thing? |

White space belongs to the layout like text. It must not change between states of the same page
unless the user wants it (panel closed, full screen). See also: no layout shift (`ui-ux-date`).

## 4. Language (UX writing, content design)

- **No stuttering.** The same word not twice in close proximity. The heading carries the term; the
  elements below only say what they do. Instead of "Examples" / "Show examples" / "Examples are …" /
  "Open my examples": "Examples" / "Show in lists" / "Made-up cases for practice …" / "Open mine".
- **Effect before object.** A label says what happens and where, not only what it is about.
- **Important first.** The first two words carry the meaning; people read beginnings, not sentences.
- **Leave out.** What the heading, the place or the element already says is not repeated
  (heuristic 8).
- **Read aloud.** If the block sounds bumpy when read aloud, rewrite it. Screen readers read exactly
  like that.

## During a review

1. Look at the page once like a newcomer: what invites a click, and what is different afterwards?
2. Go through the four groups above and name findings with the term
   ("Mapping: toggle acts on another page").
3. Severity and fix as in the entry skill under "Depth of method".
