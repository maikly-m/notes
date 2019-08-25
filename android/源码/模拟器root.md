`目录：`
  - [模拟器root
](#4544ab857485078b4e32ecdbaf6c729b)
    - [修改su
](#8a50736e40f95304f3fbde04b2b805ea)
    - [修改fs_config.c
](#b1a4b760f5f590537734e7c805b7ae69)
    - [修改com_android_internal_os_Zygote.cpp
](#948f191e722e9c709825f8a004f84d32)
    - [修改app_main.cpp
](#4ca4f5d10705dad0af7138f54b3743b8)
---
## <span id="4544ab857485078b4e32ecdbaf6c729b"/>模拟器root


版本7.1.1，修改源代码

### <span id="8a50736e40f95304f3fbde04b2b805ea"/>修改su


system/extras/su/su.c 

注释掉
```
//uid_t current_uid = getuid();
//if (current_uid != AID_ROOT && current_uid != AID_SHELL) error(1, 0, "not allowed");
```

### <span id="b1a4b760f5f590537734e7c805b7ae69"/>修改fs_config.c


system/core/libcutils/fs_config.c

权限修改为06755
```
/* the following two files are INTENTIONALLY set-uid, but they
 * are NOT included on user builds. */
{ 06755, AID_ROOT,      AID_SHELL,     0, "system/xbin/su" },
```

### <span id="948f191e722e9c709825f8a004f84d32"/>修改com_android_internal_os_Zygote.cpp


frameworks/base/core/jni/com_android_internal_os_Zygote.cpp

注释掉
```
static void DropCapabilitiesBoundingSet(JNIEnv* env) {
/*
  for (int i = 0; prctl(PR_CAPBSET_READ, i, 0, 0, 0) >= 0; i++) {
    int rc = prctl(PR_CAPBSET_DROP, i, 0, 0, 0);
    if (rc == -1) {
      if (errno == EINVAL) {
        ALOGE("prctl(PR_CAPBSET_DROP) failed with EINVAL. Please verify "
              "your kernel is compiled with file capabilities support");
      } else {
        RuntimeAbort(env, __LINE__, "prctl(PR_CAPBSET_DROP) failed");
      }
    }
  }
*/
}
```

### <span id="4ca4f5d10705dad0af7138f54b3743b8"/>修改app_main.cpp


frameworks/base/cmds/app_process/app_main.cpp

注释掉
```
/*  
    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) < 0) {
        // Older kernels don't understand PR_SET_NO_NEW_PRIVS and return
        // EINVAL. Don't die on such kernels.
        if (errno != EINVAL) {
            LOG_ALWAYS_FATAL("PR_SET_NO_NEW_PRIVS failed: %s", strerror(errno));
            return 12;
        }
    }
*/
```