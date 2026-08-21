class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def normalizeLocalName(localName: str) -> str:
            localName = localName.replace('.', '')

            idx = localName.find('+')
            if idx == -1:
                return localName
            else:
                localName = localName[0:idx]

            return localName

        
        uniqueEmails = set()

        for email in emails:
            emailParts = email.split('@')

            if len(emailParts) != 2:
                continue
            
            localName = emailParts[0]
            domainName = emailParts[1]

            localName = normalizeLocalName(localName)

            normalizedEmail = localName + '@' + domainName
            uniqueEmails.add(normalizedEmail)
        
        print(uniqueEmails)
        return len(uniqueEmails)

