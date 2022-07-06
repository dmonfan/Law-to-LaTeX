# Law to LaTeX: Bill Parser
# by David Fan

# Simple python program that turns plain text bill text to LaTeX.

# An alternative to reading bills through a browser
# Works with single section, no multiple sections
# Tested on single section which was new bill text instead of strikethroughs.
# Probably will fail on sections that contain strikethroughs

# Usage: Replace billtext with text section from congress.gov
# This might be from a page with extension .htm
# Pay attention to indentations! They are needed for the program to work.
# If tex fails to typeset it is probably for this reason, i.e. enumeration.
# Put output into tex file and typeset.

# Text may require further processing before using this script.

# Additional formatting and knowledge of LaTeX might be required.

# Notes:

# This works best if there are less than or equal to (p) subsections
# Otherwise, in the Contents section it will not fit on one page.

# In a bill a section is the title here and subsections are sections.

# Bill Text Format Requirements:
# 1. The text must start with a line with no indentations.
# 2. This line must be a title that is only 1 line long.
# 3. There is a space before the next heading sections.
# 4. The depth goes to (a)(1)(A) but no further. 3 levels. Simple text.
# 5. The text must not have any other newlines in between text.

# Parser generates a title that is not really necessary.
# The desired sections are the section text and enumerations.

def countspaces(str):
    count = 0
    for i in range(len(str)):
        if(str[i].isspace()):
            count += 1
        else:
            break
    return count

billtext = '''SEC. 2208. AI SCHOLARSHIP-FOR-SERVICE ACT.

    (a) Definitions.--In this section:
            (1) Artificial intelligence.--The term ``artificial 
        intelligence'' or ``AI'' has the meaning given the term 
        ``artificial intelligence'' in section 238(g) of the John S. 
        McCain National Defense Authorization Act for Fiscal Year 2019 
        (10 U.S.C. 2358 note).
            (2) Executive agency.--The term ``executive agency'' has 
        the meaning given the term ``Executive agency'' in section 105 
        of title 5, United States Code.
            (3) Registered internship.--The term ``registered 
        internship'' means a Federal Registered Internship Program 
        coordinated through the Department of Labor.
    (b) In General.--The Director, in coordination with the Director of 
the Office of Personnel Management, the Director of the National 
Institute of Standards and Technology, and the heads of other agencies 
with appropriate scientific knowledge, shall establish a Federal 
artificial intelligence scholarship-for-service program (referred to in 
this section as the Federal AI Scholarship-for-Service Program) to 
recruit and train artificial intelligence professionals to lead and 
support the application of artificial intelligence to the missions of 
Federal, State, local, and Tribal governments.
    (c) Qualified Institution of Higher Education.--The Director, in 
coordination with the heads of other agencies with appropriate 
scientific knowledge, shall establish criteria to designate qualified 
institutions of higher education that shall be eligible to participate 
in the Federal AI Scholarship-for-Service program. Such criteria shall 
include--
            (1) measures of the institution's demonstrated excellence 
        in the education of students in the field of artificial 
        intelligence; and
            (2) measures of the institution's ability to attract and 
        retain a diverse and non-traditional student population in the 
        fields of science, technology, engineering, and mathematics, 
        which may include the ability to attract women, minorities, and 
        individuals with disabilities.
    (d) Program Description and Components.--The Federal AI 
Scholarship-for-Service Program shall--
            (1) provide scholarships through qualified institutions of 
        higher education to students who are enrolled in programs of 
        study at institutions of higher education leading to degrees or 
        concentrations in or related to the artificial intelligence 
        field;
            (2) provide the scholarship recipients with summer 
        internship opportunities, registered internships, or other 
        meaningful temporary appointments in the Federal workforce 
        focusing on AI projects or research;
            (3) prioritize the employment placement of scholarship 
        recipients in executive agencies;
            (4) identify opportunities to promote multi-disciplinary 
        programs of study that integrate basic or advanced AI training 
        with other fields of study, including those that address the 
        social, economic, legal, and ethical implications of human 
        interaction with AI systems; and
            (5) support capacity-building education research programs 
        that will enable postsecondary educational institutions to 
        expand their ability to train the next-generation AI workforce, 
        including AI researchers and practitioners.
    (e) Scholarship Amounts.--Each scholarship under subsection (d) 
shall be in an amount that covers the student's tuition and fees at the 
institution for not more than 3 years and provides the student with an 
additional stipend.
    (f) Post-award Employment Obligations.--Each scholarship recipient, 
as a condition of receiving a scholarship under the program, shall 
enter into an agreement under which the recipient agrees to work for a 
period equal to the length of the scholarship, following receipt of the 
student's degree, in the AI mission of--
            (1) an executive agency;
            (2) Congress, including any agency, entity, office, or 
        commission established in the legislative branch;
            (3) an interstate agency;
            (4) a State, local, or Tribal government, which may include 
        instruction in AI-related skill sets in a public school system; 
        or
            (5) a State, local, or Tribal government-affiliated 
        nonprofit entity that is considered to be critical 
        infrastructure (as defined in section 1016(e) of the USA 
        Patriot Act (42 U.S.C. 5195c(e))).
    (g) Hiring Authority.--
            (1) Appointment in excepted service.--Notwithstanding any 
        provision of chapter 33 of title 5, United States Code, 
        governing appointments in the competitive service, an executive 
        agency may appoint an individual who has completed the eligible 
        degree program for which a scholarship was awarded to a 
        position in the excepted service in the executive agency.
            (2) Noncompetitive conversion.--Except as provided in 
        paragraph (4), upon fulfillment of the service term, an 
        employee appointed under paragraph (1) may be converted 
        noncompetitively to term, career-conditional, or career 
        appointment.
            (3) Timing of conversion.--An executive agency may 
        noncompetitively convert a term employee appointed under 
        paragraph (2) to a career-conditional or career appointment 
        before the term appointment expires.
            (4) Authority to decline conversion.--An executive agency 
        may decline to make the noncompetitive conversion or 
        appointment under paragraph (2) for cause.
    (h) Eligibility.--To be eligible to receive a scholarship under 
this section, an individual shall--
            (1) be a citizen or lawful permanent resident of the United 
        States;
            (2) demonstrate a commitment to a career in advancing the 
        field of AI;
            (3) be--
                    (A) a full-time student in an eligible degree 
                program at a qualified institution of higher education, 
                as determined by the Director;
                    (B) a student pursuing a degree on a less than 
                full-time basis, but not less than half-time basis; or
                    (C) an AI faculty member on sabbatical to advance 
                knowledge in the field; and
            (4) accept the terms of a scholarship under this section.
    (i) Conditions of Support.--
            (1) In general.--As a condition of receiving a scholarship 
        under this section, a recipient shall agree to provide the 
        qualified institution of higher education with annual 
        verifiable documentation of post-award employment and up-to-
        date contact information.
            (2) Terms.--A scholarship recipient under this section 
        shall be liable to the United States as provided in subsection 
        (k) if the individual--
                    (A) fails to maintain an acceptable level of 
                academic standing at the applicable institution of 
                higher education, as determined by the Director;
                    (B) is dismissed from the applicable institution of 
                higher education for disciplinary reasons;
                    (C) withdraws from the eligible degree program 
                before completing the program;
                    (D) declares that the individual does not intend to 
                fulfill the post-award employment obligation under this 
                section; or
                    (E) fails to fulfill the post-award employment 
                obligation of the individual under this section.
    (j) Monitoring Compliance.--As a condition of participating in the 
program, a qualified institution of higher education shall--
            (1) enter into an agreement with the Director to monitor 
        the compliance of scholarship recipients with respect to their 
        post-award employment obligations; and
            (2) provide to the Director, on an annual basis, the post-
        award employment documentation required under subsection (i) 
        for scholarship recipients through the completion of their 
        post-award employment obligations.
    (k) Amount of Repayment.--
            (1) Less than 1 year of service.--If a circumstance 
        described in subsection (i)(2) occurs before the completion of 
        1 year of a post-award employment obligation under this 
        section, the total amount of scholarship awards received by the 
        individual under this section shall--
                    (A) be repaid; or
                    (B) be treated as a loan to be repaid in accordance 
                with subsection (l).
            (2) 1 or more years of service.--If a circumstance 
        described in subparagraph (D) or (E) of subsection (i)(2) 
        occurs after the completion of 1 or more years of a post-award 
        employment obligation under this section, the total amount of 
        scholarship awards received by the individual under this 
        section, reduced by the ratio of the number of years of service 
        completed divided by the number of years of service required, 
        shall--
                    (A) be repaid; or
                    (B) be treated as a loan to be repaid in accordance 
                with subsection (l).
    (l) Repayments.--A loan described in subsection (k) shall--
            (1) be treated as a Federal Direct Unsubsidized Stafford 
        Loan under part D of title IV of the Higher Education Act of 
        1965 (20 U.S.C. 1087a et seq.); and
            (2) be subject to repayment, together with interest thereon 
        accruing from the date of the scholarship award, in accordance 
        with terms and conditions specified by the Director (in 
        consultation with the Secretary of Education).
    (m) Collection of Repayment.--
            (1) In general.--In the event that a scholarship recipient 
        is required to repay the scholarship award under this section, 
        the qualified institution of higher education providing the 
        scholarship shall--
                    (A) determine the repayment amounts and notify the 
                recipient and the Director of the amounts owed; and
                    (B) collect the repayment amounts within a period 
                of time as determined by the Director, or the repayment 
                amounts shall be treated as a loan in accordance with 
                subsection (l).
            (2) Returned to treasury.--Except as provided in paragraph 
        (3), any repayment under this subsection shall be returned to 
        the Treasury of the United States.
            (3) Retain percentage.--A qualified institution of higher 
        education may retain a percentage of any repayment the 
        institution collects under this subsection to defray 
        administrative costs associated with the collection. The 
        Director shall establish a fixed percentage that will apply to 
        all eligible entities, and may update this percentage as 
        needed, in the determination of the Director.
    (n) Exceptions.--The Director may provide for the partial or total 
waiver or suspension of any service or payment obligation by an 
individual under this section whenever compliance by the individual 
with the obligation is impossible or would involve extreme hardship to 
the individual, or if enforcement of such obligation with respect to 
the individual would be unconscionable.
    (o) Public Information.--
            (1) Evaluation.--The Director, in coordination with the 
        Director of the Office of Personnel Management, shall annually 
        evaluate and make public, in a manner that protects the 
        personally identifiable information of scholarship recipients, 
        information on the success of recruiting individuals for 
        scholarships under this section and on hiring and retaining 
        those individuals in the public sector AI workforce, including 
        information on--
                    (A) placement rates;
                    (B) where students are placed, including job titles 
                and descriptions;
                    (C) salary ranges for students not released from 
                obligations under this section;
                    (D) how long after graduation students are placed;
                    (E) how long students stay in the positions they 
                enter upon graduation;
                    (F) how many students are released from 
                obligations; and
                    (G) what, if any, remedial training is required.
            (2) Reports.--The Director, in coordination with the Office 
        of Personnel Management, shall submit, not less frequently than 
        once every 3 years, to the Committee on Homeland Security and 
        Governmental Affairs of the Senate, the Committee on Commerce, 
        Science, and Transportation of the Senate, the Committee on 
        Science, Space, and Technology of the House of Representatives, 
        and the Committee on Oversight and Reform of the House of 
        Representatives a report, including the results of the 
        evaluation under paragraph (1) and any recent statistics 
        regarding the size, composition, and educational requirements 
        of the Federal AI workforce.
            (3) Resources.--The Director, in coordination with the 
        Director of the Office of Personnel Management, shall provide 
        consolidated and user-friendly online resources for prospective 
        scholarship recipients, including, to the extent practicable--
                    (A) searchable, up-to-date, and accurate 
                information about participating institutions of higher 
                education and job opportunities related to the AI 
                field; and
                    (B) a modernized description of AI careers.
    (p) Refresh.--Not less than once every 2 years, the Director, in 
coordination with the Director of the Office of Personnel Management, 
shall review and update the Federal AI Scholarship-for-Service Program 
to reflect advances in technology.'''

# Translate & and $

billtext = billtext.replace('$', '\\$')
billtext = billtext.replace('&', '\\&')

# Split the bill into a list of lines that will be processed

splitbilltext = billtext.splitlines()

# Maybe don't keepends & use join with '\n' instead

# Some acronyms should not be put in title case.

title = '\\' + 'title' + '{' + splitbilltext[0].split(maxsplit=2)[-1] + '}'

newsplitbilltext = []

newsplitbilltext.append(title)

# On the first pass we deal with section and item tags.
# On the second pass we add the enumeration beginning and end tags.
# On the third and fourth pass we bold text and translate em dashes.
# The third pass relies on the first pass.

# First Pass

# This works only upto two enumeration environments.

for line in splitbilltext[1:]:

	indent = countspaces(line)
	if indent == 4:
		dotindex = line.find('.')
		line = line.replace('.','.}', 1)
		paran = '(' + line[5] + ') '
		line = line.replace(paran, '\\section{', 1)
		line = line.replace('--','')
		newsplitbilltext.append(line)
	elif indent == 12:
		paran = '(' + line[13] + ')'
		line = line.replace(paran, '\\item', 1)
		newsplitbilltext.append(line)
	elif indent == 20:
		paran = '(' + line[21] + ')'
		line = line.replace(paran, '\\item', 1)
		newsplitbilltext.append(line)
	else:
		newsplitbilltext.append(line)

# Second Pass

# An enumeration block is indented by 8 with paragraphs indented by 4
# relative to the indentation before the enumeration.
# Thus if the indentation returns ever by a multiple of 8 relative to the first indentation,
# write an end enumeration for each multiple

# Example Indents
# 0
# 0
# 4
# 12 insert begin enumeration environment
# 8
# ...
# If at the end of the run and an indent of 4 is not reached,
# add an endtag but otherwise if 4 is reached add an endtag there
# enumlevel = 0, then 1, possibly 2.

enumlevel = 0
lastindent = 0

newsplitbilltext2 = []

enumstarttag = '\\begin{enumerate}'
enumendtag = '\\end{enumerate}'

for line in newsplitbilltext:
	indent = countspaces(line)

	if (indent - lastindent >= 8):
		newsplitbilltext2.append(enumstarttag)
		enumlevel += 1
		newsplitbilltext2.append(line)
	elif ((4 + 8 * enumlevel) - indent >= 8):
		numberofendtags = ((4 + 8 * enumlevel) - indent) / 8
		while(numberofendtags > 0):
			newsplitbilltext2.append(enumendtag)
			enumlevel += -1
			numberofendtags += -1
		newsplitbilltext2.append(line)
	else:
		newsplitbilltext2.append(line)

	lastindent = indent

while(enumlevel > 0):
	newsplitbilltext2.append(enumendtag)
	enumlevel += -1

# Third Pass: Bold headings

# The dot and item indices are meant to check against
# sentences that begin with proper nouns.
# If a heading wraps around a line this will not work.

newsplitbilltext3 = []

for line in newsplitbilltext2:
    itemindex = line.find('\\item')
    dotindex = line.find('.')
    if(itemindex and dotindex > 0):
        if (line[itemindex+6].isupper()):
            line = line.replace("\\item", "\\item {\\bf")
            line = line.replace('.', '.}', 1)
    newsplitbilltext3.append(line)

final = '\n'.join(newsplitbilltext3)

# Fourth Pass: Translate em dashes

final = final.replace('--','---')

print(final)