function compress_string(s) {
    let count = 1
    let res = ""
    for (var i = 0; i < s.length; i++) {
        if (i < s.length - 1) {
            if (s[i] == s[i + 1]) {
                count += 1
            } else {
                res += s[i] + String(count)
                count = 1
            }
        } else {
            res += s[i] + String(count)
        }
    }
    console.log(res)
}

compress_string("aabacbc")