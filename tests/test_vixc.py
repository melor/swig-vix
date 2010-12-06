from vix import vixc

def test_connect():
	username = "foo"
	password = "bar"
	job_handle = vixc.VixHost_Connect(
		vixc.VIX_API_VERSION,
		vixc.VIX_SERVICEPROVIDER_VMWARE_VI_SERVER,
		"https://localhost:12345/sdk",
                0, # int hostPort,
                username, #const char *userName,
                password, #const char *password,
                0, #VixHostOptions options,
                vixc.VIX_INVALID_HANDLE, #VixHandle propertyListHandle,
                None, #VixEventProc *callbackProc,
                None, #void *clientData
		)

	print "job handle: %r" % job_handle
	host_handle = vixc.new_VixPropertyIDp()
	#host_handle = vixc.ptrcreate(int)
	err = vixc.VixJob_Wait(
		job_handle,
		vixc.VIX_PROPERTY_JOB_RESULT_HANDLE,
		host_handle,
		vixc.VIX_PROPERTY_NONE
		)

	print "host handle: %r, err=%r" % (host_handle, err)
	vixc.Vix_ReleaseHandle(job_handle)

	disco = vixc.VixHost_Disconnect(vixc.VixPropertyIDp_value(host_handle))
	print "disco: %r" % disco
	vixc.delete_VixPropertyIDp(host_handle)
