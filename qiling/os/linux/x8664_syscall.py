#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

dict_x8664_linux_syscall = {
    0x00 : "ql_syscall_read",
    0x01 : "ql_syscall_write",
    0x02 : "ql_syscall_open",
    0x03 : "ql_syscall_close",
    0x04 : "ql_syscall_stat",
    0x05 : "ql_syscall_fstat",
    0x06 : "ql_syscall_lstat",
    0x08 : "ql_syscall_lseek",
    0x09 : "ql_syscall_mmap2",
    0x0A : "ql_syscall_mprotect",
    0x0A : "ql_syscall_mprotect",
    0x0B : "ql_syscall_munmap",
    0x0C : "ql_syscall_brk",
    0x0D : "ql_syscall_rt_sigaction",
    0x0E : "ql_syscall_rt_sigprocmask",
    0x10 : "ql_syscall_ioctl",
    0x11 : "ql_syscall_pread64",
    0x14 : "ql_syscall_writev",
    0x15 : "ql_syscall_access",
    0x23 : "ql_syscall_nanosleep",
    0x27 : "ql_syscall_getpid",
    0x29 : "ql_syscall_socket",
    0x2B : "ql_syscall_accept",
    0x31 : "ql_syscall_bind",
    0x32 : "ql_syscall_listen",
    0x36 : "ql_syscall_setsockopt",
    0x38 : "ql_syscall_clone",
    0x3B : "ql_syscall_execve",
    0x3C : "ql_syscall_exit",
    0x3F : "ql_syscall_uname",
    0x48 : "ql_syscall_fcntl",
    0x4E : "ql_syscall_getdents",
    0x4F : "ql_syscall_getcwd",
    0x59 : "ql_syscall_readlink",
    0x66 : "ql_syscall_getuid",
    0x68 : "ql_syscall_getgid",
    0x6B : "ql_syscall_geteuid",
    0x6C : "ql_syscall_getegid",
    0x6E : "ql_syscall_getppid",
    0x9E : "ql_syscall_archprctl",
    0xDA : "ql_syscall_set_tid_address",
    0xE7 : "ql_syscall_exit_group",
    0x0101 : "ql_syscall_openat",
    0x0111 : "ql_syscall_set_robust_list",
    0x010D : "ql_syscall_faccessat",
    0x012E : "ql_syscall_prlimit64",
}
