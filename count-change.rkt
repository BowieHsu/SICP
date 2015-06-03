(define (count-change amount) (cc amount 5))
(define (cc amount kinds-of-coins ))
(cond ((= amount 0) 1)
      ((or (< amount 0) (= kinds-of-coins 0)) 0 )
      (else(+ (cc amount 
                  (-)))))
