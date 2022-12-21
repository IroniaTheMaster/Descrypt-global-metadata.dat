Interceptor.attach(Module.findExportByName(null, 'dlopen'), {
	onEnter: function(args) {
		this.path = args[0].readUtf8String();
	},
	onLeave: function(retval) {
		if(this.path.indexOf('libil2cpp.so') !== -1) {
			var il2cpp = Module.findBaseAddress('libil2cpp.so');
			console.error('[!] il2cpp : ' + il2cpp);
			var LoadMetaDataFile = il2cpp.add(0xValue);
			Interceptor.attach(LoadMetaDataFile, {
				onLeave: function(retval) {
					console.error('[!] LoadMetaDataFile retval : ' + retval);
				}
			});
		}
	}
});
//https://velog.io/@koo00/17
