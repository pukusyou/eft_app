function check(){var a=$("#mail").val(),b=$("#subject").val(),c=$("#body").val();if(!/^[a-zA-Z0-9_+-]+(.[a-zA-Z0-9_+-]+)*@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/.test(a))return alert("\u30e1\u30fc\u30eb\u30a2\u30c9\u30ec\u30b9\u304c\u6b63\u3057\u304f\u3042\u308a\u307e\u305b\u3093"),!1;if(3>a.length)return alert("\u30e1\u30fc\u30eb\u30a2\u30c9\u30ec\u30b9\u304c\u77ed\u3059\u304e\u307e\u3059"),!1;if(5>b.length)return alert("\u4ef6\u540d\u306f5\u6587\u5b57\u4ee5\u4e0a\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044"),
!1;if(10>c.length)return alert("\u672c\u6587\u306f10\u6587\u5b57\u4ee5\u4e0a\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044"),!1};
